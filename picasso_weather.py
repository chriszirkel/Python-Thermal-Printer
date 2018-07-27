#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import calendar
import urllib, json

# Dumps one forecast line to the printer
def forecast(idx):

    #date = datetime.fromtimestamp(int(data['daily']['data'][idx]['time']))

    forecast = data["body"]["item"]["forecast"][idx]

    day     = forecast["day"]
    lo      = forecast["low"]
    hi      = forecast["high"]
    cond    = forecast["text"]
    printer.print(day + ': low ' + str(lo) )
    printer.print(deg)
    printer.print(' high ' + str(hi))
    printer.print(deg)
    printer.println(' ' + cond.replace(u'\u2013', '-').encode('utf-8')) # take care of pesky unicode dash

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
deg     = chr(0xf8) # Degree symbol on thermal printer

#url = "https://api.darksky.net/forecast/"+API_KEY+"/"+LAT+","+LONG+"?exclude=[alerts,minutely,hourly,flags]&units=us"
url = "https://s2ia2zza6j.execute-api.us-east-1.amazonaws.com/latest/weather?city=mannheim&countryCode=de"
response = urllib.urlopen(url)
data = json.loads(response.read())

# Print heading
printer.inverseOn()
#printer.print('{:^32}'.format("DarkSky.Net Forecast"))
printer.println('{:^32}'.format(data["body"]["title"].replace("Yahoo! ", "")))
printer.inverseOff()

# Print current conditions
printer.boldOn()
printer.print('{:^32}'.format('Current conditions:'))
printer.boldOff()


temp = data["body"]["item"]["condition"]["temp"]
printer.print(temp)
printer.print(deg)

cond = data["body"]["item"]["condition"]["text"]
printer.println(' ' + cond)

# Print forecast
printer.boldOn()
printer.print('{:^32}'.format('Forecast:'))
printer.boldOff()
forecast(0)
forecast(1)

printer.feed(3)
