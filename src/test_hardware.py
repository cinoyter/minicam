
#from picamera import PiCamera                                                                                                                                                                                                                

import RPi.GPIO as GPIO

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

GPIO.setmode(GPIO.BCM)



LEFT = 18;
SELECT = 15;
RIGHT = 14;


def button_callback(channel):

    if(channel == LEFT):
        word = "Left"
    elif (channel == SELECT):
        word = "Select"
    elif (channel == RIGHT):
        word = "Right"

    print(word)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30,10), word, fill="white")

serial = i2c(port=1, address=0x3c)
device = ssd1306(serial, width=128, height=32)


GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(14, GPIO.RISING, callback=button_callback)
GPIO.add_event_detect(15, GPIO.RISING, callback=button_callback)
GPIO.add_event_detect(18, GPIO.RISING, callback=button_callback)



message=input("PRess enter to quit")
#.cleanup()
# while True:
#     if GPIO.input(10) == GPIO.HIGH:
#         print('Button!');
