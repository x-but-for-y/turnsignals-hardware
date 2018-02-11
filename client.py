import requests, json
import serial
import time
from gpio_96boards import GPIO

LEFT = GPIO.gpio_id('GPIO_B')
RIGHT = GPIO.gpio_id('GPIO_A')

pins = (
    (LEFT, 'out'),
    (RIGHT, 'out')
)


def blink(pin):
    with GPIO(pins) as gpio:
        for i in range(3):
            gpio.digital_write(pin[0], GPIO.HIGH)
            time.sleep(i)
            gpio.digital_write(pin[0], GPIO.LOW)
            time.sleep(1)


while True:
    try:
        signals = json.loads(requests.get('http://983f4cb9.ngrok.io').text)
        if signals['right']:
            blink(pins[1])
            reqeusts.get('http://983f4cb9.ngrok.io/right')
        elif signals['left']:
            reqeusts.get('http://983f4cb9.ngrok.io/left')
            blink(pins[0])

        time.sleep(1)
    except:
       print "Rip JSON"

