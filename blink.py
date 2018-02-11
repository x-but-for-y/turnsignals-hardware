#!/usr/bin/python
import time

from gpio_96boards import GPIO

GPIO_B = GPIO.gpio_id('GPIO_B')
GPIO_A = GPIO.gpio_id('GPIO_A')

pins = (
    (GPIO_A, 'out'),
    (GPIO_B, 'out')
)


def blink(gpio):
    for pin in pins:
        print pin
        for i in range(3):
            gpio.digital_write(pin[0], GPIO.HIGH)
            time.sleep(i)
            gpio.digital_write(pin[0], GPIO.LOW)
            time.sleep(1)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
        print gpio
        blink(gpio)
