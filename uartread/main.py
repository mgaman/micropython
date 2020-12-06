# This is your main script.
from machine import UART

uart = UART(0, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

while True:
    n = uart.any()
    if n > 0:
        line = uart.readline()
        print(line)
