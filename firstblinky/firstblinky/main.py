# This is your main script.
import machine
from time import sleep
led = machine.Pin(2,machine.Pin.OUT)
while True:
    led.off()
    sleep(1)
    led.on()
    sleep(1)
    print ('blink')
 