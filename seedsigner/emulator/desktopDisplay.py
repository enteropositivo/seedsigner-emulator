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
        #self.root = tk.Toplevel()
        self.root = tk.Tk()
        
        from seedsigner.controller import Controller
        controller = Controller.get_instance()
        self.root.title("SeedSigner Emulator v1.0 ("+controller.VERSION+")")

        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.geometry("520x245+200+200")
        self.root.configure(bg='orange')
        self.root.iconphoto(False, tk.PhotoImage(file='seedsigner/resources/icons/emulator_icon.png'))
        # ....


        self.label=Label(self.root)
        self.label.pack()

        self.btnL = Button(self.root, width=2, command = HardwareButtons.KEY_LEFT_PIN, bg='white')
        self.btnL.place(x=40, y=100)
        self.bindButtonClick(self.btnL)

        self.btnR = Button(self.root, width=2, command = HardwareButtons.KEY_RIGHT_PIN, bg='white')
        self.btnR.place(x=100, y=100)
        self.bindButtonClick(self.btnR)

        self.btnC = Button(self.root, width=2, command = HardwareButtons.KEY_PRESS_PIN)
        self.btnC.place(x=70, y=100)
        self.bindButtonClick(self.btnC)

        self.btnU = Button(self.root, width=2, command = HardwareButtons.KEY_UP_PIN, bg='white')
        self.btnU.place(x=70, y=70)
        self.bindButtonClick(self.btnU)

        self.btnD = Button(self.root, width=2, command = HardwareButtons.KEY_DOWN_PIN, bg='white')
        self.btnD.place(x=70, y=130)
        self.bindButtonClick(self.btnD)

        self.btn1 = Button(self.root, width=4,  command = HardwareButtons.KEY1_PIN, bg='white')
        self.btn1.place(x=400, y=50)
        self.bindButtonClick(self.btn1)

        self.btn2 = Button(self.root, width=4,  command = HardwareButtons.KEY2_PIN, bg='white')
        self.btn2.place(x=400, y=106)
        self.bindButtonClick(self.btn2)

        self.btn3 = Button(self.root, width=4,  command = HardwareButtons.KEY3_PIN, bg='white')
        self.btn3.place(x=400, y=162)
        self.bindButtonClick(self.btn3)

        self.root.resizable(width = False, height = True)
        self.root.mainloop()

        

     
 
    def bindButtonClick(self, objBtn):
        objBtn.bind("<Button-1>", self.buttonClick)

    def buttonClick(self, objBtn):
        gpioID = (objBtn.widget.config('command')[-1])
        GPIO.fire_raise_event(gpioID)


    def ShowImage(self,Image2,Xstart,Ystart):
        imwidth, imheight = Image2.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))

        self.tkimage= ImageTk.PhotoImage(Image2, master=self.root)
        self.label.configure(image=self.tkimage)
        self.label.image=self.tkimage
       
        
    def clear(self):
        """Clear contents of image buffer"""
 