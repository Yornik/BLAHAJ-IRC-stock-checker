from irc import *
import requests
import urllib3
import time
import json
import os
import random
http = urllib3.PoolManager()
channel = "#revspace"
server = "irc.freenode.net"
nickname = "BLAHAJ"

irc = IRC()
irc.connect(server, channel, nickname)

rdata = http.request('GET',
        "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/30373588",
        headers={
        'Contract': '37249',
        'Accept': 'application/vnd.ikea.iows+json;version=1.0',
        'Consumer': 'MAMMUT',
         })
pdata = json.loads(rdata.data.decode('utf-8'))

print(pdata["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])

while 1:
    text = irc.get_text()
    if text != bytes('', "utf-8"):
        print(text)
 
    if bytes("PRIVMSG", "UTF-8") in text and bytes(channel, "utf-8") in text and bytes("!BLÅHAJDelft", "UTF-8") in text:
        rdata = http.request('GET',
                "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/30373588",
                headers={
                'Contract': '37249',
                'Accept': 'application/vnd.ikea.iows+json;version=1.0',
                'Consumer': 'MAMMUT',
                 })
        pdata = json.loads(rdata.data.decode('utf-8'))
        irc.send(channel, "BLÅHAJ op vooraad in Ikea Delft: " + str(pdata["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])+ " BLÅHAJ`s.🦈")

