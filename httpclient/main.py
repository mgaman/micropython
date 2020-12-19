# This is your main script.
import network
import urequests
import settings
from time import sleep

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(settings.ssid,settings.password)
connected = False
while not connected:
    print('',end='.')
    connected = station.isconnected()
    sleep(0.1)
config = station.ifconfig()


print('IP address: '+config[0])

response = urequests.get(settings.url)
if response.status_code == 200: # good
    print(response.text)
else:
    print(str(response.status_code) + ' ' + str(response.reason))
station.disconnect()

