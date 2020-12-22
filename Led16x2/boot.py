import network
#import esp
#import webrepl

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='micropythonesp32')

#esp.osdebug(None)
#webrepl.start()
