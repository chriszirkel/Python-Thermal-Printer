#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import calendar
import urllib, json

# Dumps one forecast line to the printer
def twitter(idx):
    twitter = data["body"][idx]

    name = twitter["user"]["name"]
    screen_name = twitter["user"]["screen_name"]
    text = twitter["text"]

    printer.boldOn()
    printer.println('{:^32}'.format(name + " - " + screen_name))
    printer.boldOff()

    printer.println(text.replace(u'\2026', '...').encode('utf-8'))
    #printer.println(' ' + cond.replace(u'\u2013', '-').encode('utf-8')) # take care of pesky unicode dash

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
#deg     = chr(0xf8) # Degree symbol on thermal printer

url = "https://s2ia2zza6j.execute-api.us-east-1.amazonaws.com/latest/twitter?screen_name=realDonaldTrump"
response = urllib.urlopen(url)
data = json.loads(response.read())

# Print heading
printer.inverseOn()
printer.println('{:^32}'.format("Twitter"))
printer.inverseOff()

# Print twitter
twitter(0)
twitter(1)

printer.feed(3)
