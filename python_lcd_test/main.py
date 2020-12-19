"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
import python_lcd
from sys import platform

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
if platform == 'esp32':
   i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
elif platform == 'esp2866':
   i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
NUM_ROWS = 2
NUM_COLS = 16

lcd = python_lcd.I2cLcd(i2c, DEFAULT_I2C_ADDR, NUM_ROWS, NUM_COLS)
lcd.putstr(platform)
sleep_ms(2000)
lcd.clear()

for x in range(NUM_ROWS):
    lcd.move_to(0,x)
    lcd.putstr("ROW ")
    lcd.putstr(str(x+1))
