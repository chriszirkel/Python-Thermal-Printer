#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import calendar
import urllib, json
from unidecode import unidecode

# Dumps one forecast line to the printer
def news(idx):

    #date = datetime.fromtimestamp(int(data['daily']['data'][idx]['time']))

    news = data["body"][idx]

    name = to_ascii(news["source"]["name"])
    title = to_ascii(news["title"])

    printer.boldOn()
    printer.println('{:^32}'.format(name))
    printer.boldOff()

    printer.println(title)
    #printer.println(' ' + cond.replace(u'\u2013', '-').encode('utf-8')) # take care of pesky unicode dash

def to_ascii(text):
    return unidecode(text)

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
#deg     = chr(0xf8) # Degree symbol on thermal printer

url = "https://s2ia2zza6j.execute-api.us-east-1.amazonaws.com/latest/news?category=business&country=de"
response = urllib.urlopen(url)
data = json.loads(response.read())

# Print heading
printer.inverseOn()
printer.println('{:^32}'.format("News - Business, DE"))
printer.inverseOff()

# Print news
news(0)
news(1)

printer.feed(3)
