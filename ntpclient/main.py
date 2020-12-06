# This is your main script.
import network
import settings
import ntptime
import time 
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(settings.ssid,settings.password)
connected = False
while not connected:
    print('',end='.')
    connected = station.isconnected()
    time.sleep(0.1)
config = station.ifconfig()

lcd.putstr(config[0])
lcd.move_to(0,0)
time.sleep(3)
print('IP address: '+config[0])
print ("Time before sync: %s",str(time.localtime()))
ntptime.settime()
print ("Time after sync: %s",str(time.localtime()))
#lcd.putstr(str(time.localtime()))
now = time.localtime()
text = str(now[2])+ '/' +str(now[1])+ '/' + str(now[0])
lcd.putstr(text) 
lcd.move_to(0,1)
text = str(now[3])+ ':' + str(now[4])+ ':' + str(now[5])
lcd.putstr(text) 
station.disconnect()

