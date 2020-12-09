# This is your main script.
import machine
led = machine.Pin(2,machine.Pin.OUT) # builtin led
led.on()
ledon = False
def pininterrupt(pin):
    global ledon
    if ledon == True:
        led.off()
    else:
        led.on()
    ledon = not ledon
button = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_UP) # D5

button.irq(trigger = machine.Pin.IRQ_RISING,handler = pininterrupt)
while True:
    pass