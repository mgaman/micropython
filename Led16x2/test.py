"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def test_main():
    """Test function for verifying basic functionality."""
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2,16)
    lcd.putstr("It Works!\nSecond Line")
    sleep_ms(3000)
    lcd.clear()
    count = 0
#if __name__ == "__main__":
test_main()
