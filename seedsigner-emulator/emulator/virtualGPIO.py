######################################################################
#  virtualGPIO allows program with the same GPIO code as allways
#  to test your code on a desktop enviroment
#
#  by: @EnteroPositivo (Twitter, Gmail, GitHub)
#   
#  Code from: https://roderickvella.wordpress.com/2016/06/28/raspberry-pi-gpio-emulator/


import time


dictionaryPins = {}
raisedPin=""

class GPIO:

    #constants
    LOW = 0 
    HIGH = 1
    OUT = 2
    IN = 3
    PUD_OFF = 4
    PUD_DOWN = 5
    PUD_UP = 6
    BCM = 7

    
    
    #GPIO LIBRARY Functions
    def setmode(mode):
        time.sleep(1)
            
    def setwarnings(flag):
        pass

    def setup(channel, state, initial=-1,pull_up_down=-1):
        global dictionaryPins
        
        #check if channel is already setup
        if str(channel) in dictionaryPins:
            raise Exception('GPIO is already setup')

        if(state == GPIO.OUT):
            #GPIO is set as output, default OUT 0
            objTemp =  PIN("OUT")
            if(initial == GPIO.HIGH):
                objTemp.Out = "1"
                
            dictionaryPins[str(channel)] =objTemp
            #drawGPIOOut(channel)
            
        elif(state == GPIO.IN):
            #set input
            objTemp =  PIN("IN")
            if(pull_up_down == -1):
                objTemp.pull_up_down = "PUD_DOWN" #by default pud_down
                objTemp.In = "0"
            elif(pull_up_down == GPIO.PUD_DOWN):
                objTemp.pull_up_down = "PUD_DOWN"
                objTemp.In = "0"
             
            elif(pull_up_down == GPIO.PUD_UP):
                objTemp.pull_up_down = "PUD_UP"
                objTemp.In = "1"
                
            #drawBindUpdateButtonIn(str(channel),objTemp.In)
            dictionaryPins[str(channel)] =objTemp


    def output(channel, outmode):
        global dictionaryPins
        channel = str(channel)

        if channel not in dictionaryPins:
            #if channel is not setup
            raise Exception('GPIO must be setup before used')
        else:
            objPin = dictionaryPins[channel]
            if(objPin.SetMode == "IN"):
                #if channel is setup as IN and used as an OUTPUT
                raise Exception('GPIO must be setup as OUT')

        
        if(outmode != GPIO.LOW and outmode != GPIO.HIGH):
            raise Exception('Output must be set to HIGH/LOW')
            
        objPin = dictionaryPins[channel]
        if(outmode == GPIO.LOW):
            objPin.Out = "0"
        elif(outmode == GPIO.HIGH):
            objPin.Out = "1"


    def input(channel):
        global dictionaryPins, raisedPin
        global raisedPin


        channel = str(channel)
        
        if channel not in dictionaryPins:
            #if channel is not setup
            raise Exception('GPIO must be setup before used')
        else:
            objPin = dictionaryPins[channel]
            if(objPin.SetMode == "OUT"):
                #if channel is setup as OUTPUT and used as an INPUT
                raise Exception('GPIO must be setup as IN')
       
        objPin = dictionaryPins[channel]
        
        if (channel==raisedPin) & (raisedPin!="13") & (objPin.In == "0"):
            time.sleep(0.02)
            GPIO.risecallback(channel)
            objPin.In = "1"
            raisedPin=""
            return False

        if(objPin.In == "1"):
            return True
        elif(objPin.Out == "0"):
            return False

        
    


    def cleanup():
        pass

    def add_event_detect(channel,edge,callback):
        GPIO.risecallback=callback

    def fire_raise_event(gpioID):
        global dictionaryPins, raisedPin 

        print( "Emulator GPIO:", gpioID)
        
        objPin = dictionaryPins[str(gpioID)]
        
        objPin.In = "0"
        raisedPin=str(gpioID)
        
        if (raisedPin=="13"):
            GPIO.risecallback(gpioID)
            time.sleep(0.02)
            objPin.In = "1"
            raisedPin=""
    
        
           
            
       
class PIN():
    SetMode = "None" #IN/OUT/NONE
    Out = "0"
    pull_up_down = "PUD_OFF" #PUD_UP/PUD_DOWN/PUD_OFF
    In = "1"

    def __init__(self, SetMode):
        self.SetMode = SetMode
        self.Out = "0"    
