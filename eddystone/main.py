# This example demonstrates a simple temperature sensor peripheral.
#
# The sensor's local value updates every second, and it will notify
# any connected central every 10 seconds.

import bluetooth
import random
import struct
import time
from ble_advertising import advertising_payload
from time import sleep
import machine

from micropython import const
_IRQ_CENTRAL_CONNECT                 = const(1 << 0)
_IRQ_CENTRAL_DISCONNECT              = const(1 << 1)
# org.bluetooth.service.environmental_sensing
_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
# org.bluetooth.characteristic.temperature
_TEMP_CHAR = (bluetooth.UUID(0x2A6E), bluetooth.FLAG_READ|bluetooth.FLAG_NOTIFY,)
_ENV_SENSE_SERVICE = (_ENV_SENSE_UUID, (_TEMP_CHAR,),)

_ENV_EDDYSTONE_UUID = bluetooth.UUID(0xFEAA)
_ENV_EDDYSTONE_SERVICE = (_ENV_EDDYSTONE_UUID,(_TEMP_CHAR,),)
# org.bluetooth.characteristic.gap.appearance.xml
#_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)

class BLE_Eddystone:
    def __init__(self,ble,name='MB'):
        self._ble = ble
        self._ble.active(True)
        self._connections = set()
        ((self._handle,),) = self._ble.gatts_register_services((_ENV_EDDYSTONE_SERVICE,))        
#        self._payload = advertising_payload(name=name, services=[_ENV_EDDYSTONE_UUID])
        self._payload = advertising_payload(services=[_ENV_EDDYSTONE_UUID])  # SAVE SPACE

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)
        self._ble.gap_advertise()

    def addURL(self,prefix,url) :
        self._payload.append(6+len(url))  # length of service data
        self._payload.append(0x16)  # frame type
        self._payload.append(0xaa)   # eddystone 
        self._payload.append(0xfe)  
        self._payload.append(0x10)   # URL frame type
        self._payload.append(0)   # txpower
        self._payload.append(prefix)  # 0-3
        self._payload.extend(url)

    def dumpPayload(self):
        print([hex(i) for i in self._payload])


def demo():
    ble = bluetooth.BLE()
    eddy  = BLE_Eddystone(ble)
    eddy.addURL(0,'zickel.net')  # http:/www.zickel.net
#    print(ble.config('mac'))
    eddy.dumpPayload()
    eddy._advertise()
    while False:
        eddy._advertise()
        sleep(1)

if __name__ == '__main__':
    demo()


