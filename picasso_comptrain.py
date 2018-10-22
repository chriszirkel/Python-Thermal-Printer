#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import calendar
# import urllib
import requests
#import urllib.request
import json
from unidecode import unidecode


def comptrain(data):
    lines = data.splitlines()
    i = 0

    for line in lines:
        i += 1
        text = to_ascii(line)

        if i == 1:
            printer.boldOn()
            printer.println('{:^32}'.format(text))
            printer.boldOff()
        else:
            printer.println('{:^32}'.format(text))


def to_ascii(text):
    return unidecode(text)


# printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=5)

url = "https://8ukyst5l4f.execute-api.us-east-1.amazonaws.com/dev/comptrain/open"
# response = urllib.urlopen(url)
# data = response.read()
response = requests.get(url)
data = response.text
# with urllib.request.urlopen(url) as response:
#    data = response.read()

print(to_ascii(data))

heading = '{} {}'.format('CompTrain', datetime.today().strftime('%Y-%m-%d'))

# Print heading
# printer.inverseOn()
printer.boldOn()
printer.println('{:^32}'.format(heading))
printer.boldOff()
# printer.inverseOff()

# CompTrain
comptrain(data)

printer.feed(3)
