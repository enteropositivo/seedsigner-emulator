######################################################################
#  Seedsigner desktop display driver and button emulator
#
#  by: @EnteroPositivo (Twitter, Gmail, GitHub)



import time

from seedsigner.emulator.virtualGPIO import GPIO
from seedsigner.hardware.buttons import HardwareButtons

from tkinter import *
import tkinter as tk


from PIL import ImageTk

import threading
import os

EMULATOR_VERSION = '0.1'
        

class desktopDisplay(threading.Thread):
    """class for desktop display."""
    root=0
    def __init__(self):
        self.width = 240
        self.height = 240

        # Multithreading
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
        self.root.destroy()
        # terminate the main thread forcefully
        pid = os.getpid()
        os.kill(pid,9)

    def run(self):
        """run thread"""    
        self.root = tk.Tk()
        
        from seedsigner.controller import Controller
        controller = Controller.get_instance()
        self.root.title("SeedSigner Emulator v"+EMULATOR_VERSION+ " / "+controller.VERSION)

        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("510x245+200+200")
        self.root.configure(bg='orange')
        self.root.iconphoto(False, tk.PhotoImage(file='seedsigner/resources/icons/emulator_icon.png'))
        # ....


        self.label=Label(self.root)
        self.label.pack()

        self.joystick=Frame(self.root)
        self.joystick.pack()
        self.joystick.place(x=20, y=75)
        self.joystick.configure(bg='orange')
        


        self.btnL = Button(self.joystick, width=2, command = HardwareButtons.KEY_LEFT_PIN, bg='white')
        self.btnL.grid(row=1, column=0)
        self.bindButtonClick(self.btnL)

        self.btnR = Button(self.joystick, width=2, command = HardwareButtons.KEY_RIGHT_PIN, bg='white')
        self.btnR.grid(row=1, column=2)
        self.bindButtonClick(self.btnR)

        self.btnC = Button(self.joystick, width=2, command = HardwareButtons.KEY_PRESS_PIN)
        self.btnC.grid(row=1, column=1)
        self.bindButtonClick(self.btnC)

        self.btnU = Button(self.joystick, width=2, command = HardwareButtons.KEY_UP_PIN, bg='white')
        self.btnU.grid(row=0, column=1)
        self.bindButtonClick(self.btnU)

        self.btnD = Button(self.joystick, width=2, command = HardwareButtons.KEY_DOWN_PIN, bg='white')
        self.btnD.grid(row=2, column=1)
        self.bindButtonClick(self.btnD)

        self.btn1 = Button(self.root, width=4,  command = HardwareButtons.KEY1_PIN, bg='white')
        self.btn1.place(x=420, y=50)
        self.bindButtonClick(self.btn1)

        self.btn2 = Button(self.root, width=4,  command = HardwareButtons.KEY2_PIN, bg='white')
        self.btn2.place(x=420, y=106)
        self.bindButtonClick(self.btn2)

        self.btn3 = Button(self.root, width=4,  command = HardwareButtons.KEY3_PIN, bg='white')
        self.btn3.place(x=420, y=162)
        self.bindButtonClick(self.btn3)

        
        def key_handler(event):
            #print(event.char, event.keysym, event.keycode)
            #print(event.keycode)
            if(event.keycode==38): GPIO.fire_raise_event(HardwareButtons.KEY_UP_PIN)
            if(event.keycode==40): GPIO.fire_raise_event(HardwareButtons.KEY_DOWN_PIN)
            if(event.keycode==37): GPIO.fire_raise_event(HardwareButtons.KEY_LEFT_PIN)
            if(event.keycode==39): GPIO.fire_raise_event(HardwareButtons.KEY_RIGHT_PIN)

            if(event.keycode==97): GPIO.fire_raise_event(HardwareButtons.KEY1_PIN)
            if(event.keycode==98): GPIO.fire_raise_event(HardwareButtons.KEY2_PIN)
            if(event.keycode==99): GPIO.fire_raise_event(HardwareButtons.KEY3_PIN)

            if(event.keycode==13): GPIO.fire_raise_event(HardwareButtons.KEY_PRESS_PIN)

        self.root.bind("<Key>", key_handler)

        self.root.resizable(width = True, height = True)
        self.root.mainloop()
     
 
    def bindButtonClick(self, objBtn):
        objBtn.bind("<Button-1>", self.buttonClick)

    def buttonClick(self, objBtn):
        gpioID = (objBtn.widget.config('command')[-1])
        GPIO.fire_raise_event(gpioID)

    def setGPIO(self, pin):
        GPIO.fire_raise_event(pin)

    def ShowImage(self,Image2,Xstart,Ystart):
        while(self.root==0): time.sleep(0.1)
        imwidth, imheight = Image2.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))

        self.tkimage= ImageTk.PhotoImage(Image2, master=self.root)
        self.label.configure(image=self.tkimage)
        self.label.image=self.tkimage
       
        
    def clear(self):
        """Clear contents of image buffer"""
 