# This is your main script.
from machine import UART
import uio

src = UART(1,baudrate=9600,rx=17,tx=5)
# no buffered streams in micropython
sio = uio.TextIOWrapper(src)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while True:
    print(sio.readline())
