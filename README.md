# micropython-dweet-example
An example script with an ESP running micropython watching for dweets

A simple example of using Micropython on an ESP (8266 in this case) to connect to and internet 
connected wifi and watching the incoming tweets from Dweet.io

There are two files, one in the main.py you will need to place on your device and the other 
is an HTML file to drive the test.

For information on Dweet.io and using it see: http://dweet.io/ It's free, easy to use and there
is no registration. Dweets are public and could be see, so no personal info please! I have used 
it to send out GPS info, local IP's of IOT devices and of course collected data.

To test it, download the files (or clone the repo) Load the main.py into you favorite text
editor and change the following lines by adding your network SSID, wifi password and the 
Thing name you want to use for the DWEETS for the device. Make a name the is as unique to you 
and your device as possible. You could just generate a GUID, but I like a little whimsy in my
names.

Example name: "ThisXISXMyXpunyXlilXdeviceX11x05x1605"

Places to change in main.py:
SSID = str('YOUR-SSID', 'utf8')
PASSWD = str('YOUR-PASSWD', 'utf8')
thing_name = str('YOUR-THING-NAME', 'utf8')

Place to change in the HTML:
var THING_NAME = 'YOUR-THING-NAME'

Save the modified main.py to your MicroPython ESP device with Thonny, ampy or your preferred REPL
talking method.

At this point you should be able to load the HTML file into a browser and click the "Buzz" button
and the action you set your device to do will happen.


