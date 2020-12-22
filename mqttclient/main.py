#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

from mqtt import MQTTClient
import network, machine, os, time

import settings

def settimeout(duration): 
    pass

def msgcallback(topic,payload):
    print(topic+': '+payload)
    return

#uart = machine.UART(0, baudrate=115200)
#os.dupterm(uart)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# configure AFTER active
wlan.config(dhcp_hostname='WemosD1R32')
wlan.connect(settings.ssid,settings.password)

connected = False
while not connected:
    print('',end='.')
    connected = wlan.isconnected()
    time.sleep(0.1)
config = wlan.ifconfig()
print(config[0])

print("Connected to Wifi\n")
client = MQTTClient("demo", settings.mttqBroker, port=1883, user = settings.mqttUser, password = settings.mqttPassword)
client.settimeout = settimeout
client.connect()
# Must set callback before subscribe 
client.set_callback(msgcallback)
client.subscribe('test')

onoff = True
while True:
    if onoff:
        print("Sending ON")
        client.publish("/lights", "ON")
    else:
        print("Sending OFF")
        client.publish("/lights", "OFF")
    time.sleep(1)
    onoff = not onoff
    client.check_msg()
