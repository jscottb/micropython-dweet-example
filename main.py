#
#   ESP8266 Buzzer via Dweet.IO.
#
#   Goal in life:
#     Drives buzzer (or your device) from an ESP8266 and Dweet.IO.
#
#   Written By - Scott Beasley 2018.
#
#   Public domain. Free to use or change. Enjoy :)
#

import network
import urequests
from machine import Pin, RTC
from time import sleep

# Globals

# Add your wifi info here...
SSID = str('YOUR-SSID', 'utf8')
PASSWD = str('YOUR-PASSWD', 'utf8')

# Add your Dweet thing name (See http://dweet.io for more info)
thing_name = str('YOUR-THING-NAME', 'utf8')

# Var to hold last dt a dweet was received.
last_dweet_dt = str('', 'utf8')

def wifi_connect ():
    global SSID, PASSWD
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWD)
        while not sta_if.isconnected():
           pass  # Dwell until we get connected or an error.
        
    print('network settings:', sta_if.ifconfig())
    
def wait_to_buzz ():
    global last_dweet_dt, thing_name
     
    while True:
        # Check for a new Dweet every few seconds. There is a speed limit, but 
        # I'm unsure what is.  
        sleep (15)
        r = urequests.get ("http://dweet.io/get/latest/dweet/for/" + thing_name)

        # If the request was good, then get the data sent back.
        if r.status_code == 200:
            ret_json = r.json( )
            buzz = str(ret_json['with'][0]['content']['buzz'], 'utf8')
            created_dt = str(ret_json['with'][0]['created'], 'utf8')

            # Do the action only if the last execute time is different.
            if buzz == 'y' and created_dt != last_dweet_dt:
                print("Buzzzz")
                # Could save in EEPROM for restart carry over
                last_dweet_dt = created_dt 
                buzzer.value(1)
                sleep(2)
                buzzer.value (0)
        
        r.close( )

# Let's get it all started up...
wifi_connect( )

# GPIO13 (D7) set to OUTPUT
buzzer = Pin(13, Pin.OUT, pull=0)

# Do a quick job of the buzzer on startup
buzzer.value(0)
buzzer.value(1)
buzzer.value (0)

# Wait for something to do 
wait_to_buzz( )

        
        
        
        
        
        
