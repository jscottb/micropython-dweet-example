# micropython-dweet-example

A simple example of using Micropython on an ESP (8266 in this case) to connect to an internet 
connected wifi and watch for incoming "Dweets" from Dweet.io

There are two files, one is main.py that you will need to place on your device and the other 
is an HTML file to drive the test.

For information on Dweet.io and using it see: http://dweet.io/ It's free, easy to use and there
is no registration needed. Dweets are public and could be seen by others, so no personal info please! 
I have used it to send out GPS info, local IP's of IOT devices and of course collected data.

To test it, download the files (or clone the repo here), load the main.py into your favorite text
editor and change the lines below by adding your network SSID, wifi password and the 
Thing name you want to use for the DWEETS for the device. Make a name the is as unique to you 
and your device as possible. You could just generate a GUID and use that for the name, but I like
a little whimsy in my names.

Example name: "ThisXISXMyXpunyXlilXdeviceX11x05x1605"<br>

<b>Places to change in main.py:<br>
SSID = str('YOUR-SSID', 'utf8')<br>
PASSWD = str('YOUR-PASSWD', 'utf8')<br>
thing_name = str('YOUR-THING-NAME', 'utf8')<br>

Place to change in the HTML:<br>
var THING_NAME = 'YOUR-THING-NAME'<br></b>

Save the modified main.py to your MicroPython ESP device with Thonny, ampy or your preferred REPL
talking method.

At this point you should be able to load the HTML file into a browser and click the "Buzz" button
and the action you set your device to do will happen.


