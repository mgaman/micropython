"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
import dht
from esp8266_i2c_lcd import I2cLcd
import settings

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

#lcd.custom_char(1,[0x0e,0x0a,0x0e,0,0,0,0,0]) # degree symbol
#lcd.custom_char(1,[0x1c,0x14,0x1c,0,0,0,0,0]) # degree symbol
lcd.custom_char(1,[0x18,0x18,0,0xf,8,8,8,0xf]) # degree symbol
d = dht.DHT22(Pin(0))  # D3
#lcd.backlight_off()
lcd.
while True:
   d.measure()
   t = d.temperature()
   h = d.humidity()
   print(t,',',h)
   lcd.clear()
   lcd.putstr('Temp     ')
   lcd.putstr(str(t))
#   lcd.putstr('\x01C')
   lcd.putstr('\x01')
   lcd.move_to(0,1)
   lcd.putstr('Humidity ')
   lcd.putstr(str(h))
   lcd.putstr('%')
   sleep_ms(10000)
