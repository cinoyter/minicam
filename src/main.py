


#from picamera import PiCamera

import time
import RPi.GPIO as GPIO

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

from time import sleep

from rotaryencoder import RotaryEncoder

import panes

GPIO.setmode(GPIO.BCM)


serial = i2c(port=1, address=0x3c)
device = ssd1306(serial, width=128, height=32)


class Camera_UI():

    ROTARY_PINS = {
        'A': 14,
        'B': 18,
        'BUTTON': 15
    }
    
    PINS = {
        # 'SELECT': 15
    }
    
    def __init__(self):
        print('init')
        
        self.rotary_pin_status = {}
        
        for name, pin in self.PINS.items():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(pin, GPIO.RISING, callback=self.button_callback)

        self.encoder = RotaryEncoder(self.ROTARY_PINS['A'], self.ROTARY_PINS['B'],
                                     callback=self.rotary_callback,
                                     buttonPin=self.ROTARY_PINS['BUTTON'],
                                     buttonCallback=self.button_callback
        )


        print(self.rotary_pin_status)
        self.active = panes.Pane_Left(device)
        self.active.ready()

        
    def rotary_callback(self, delta):
        print('rotary', delta)
        
        if(delta == 1):
            action = self.active.left()
        elif(delta == -1):
            action = self.active.right()

        if isinstance(action, str):
            self.transition(action)
        
        

        
        
    def button_callback(self, channel):
        print('button_callback', channel)
        # if(channel == self.PINS['LEFT']):
        #     action = self.active.left()
        # elif (channel == self.PINS['SELECT']):
        #     action = self.active.select()
        # elif (channel == self.PINS['RIGHT']):
        #     action = self.active.right()

        # if isinstance(action, str):
        #     self.transition(action)
        

    def transition(self, pane):
        print('transition');
        NextPane = getattr(panes, pane)
        self.active.destroy()

        self.active = NextPane(device)
        self.active.ready()
    

ui = Camera_UI()

while 1:
    time.sleep(0.01)
