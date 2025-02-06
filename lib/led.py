from machine import Pin
from utime import sleep

led = Pin(2, Pin.OUT)

def led_blink_error(seconds):
  seconds_passed = 0
  while seconds_passed < seconds:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    seconds_passed += 0.2

def led_blink_success(seconds):
  seconds_passed = 0
  while seconds_passed < seconds:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    seconds_passed += 2

