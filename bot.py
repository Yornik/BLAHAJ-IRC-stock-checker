# YHeyl<yornik@yornik.nl> MIT liscense
# thanks to <mrngm> For help with the headers
## todo - YH
# - pep 8
# - more parameters (difrent articels and stores/countries would be nice)
# - docker file 
# - more IKEA funtions (opening times, price, location in pickupbay)
# - pushing important events as a messege like a decrese or increse in stock
# - some nice help text
# - Maybe in futere ordering via private messages
# - Intregration with TRÅDFRI RGB bulb
# - running it in a lack rack


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
nickname = "BLAHAJ_Delft_Bot"

irc = IRC()
irc.connect(server, channel, nickname)
## Test not needed in production 
# rdata = http.request('GET',
#         "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/30373588",
#         headers={
#         'Contract': '37249',
#         'Accept': 'application/vnd.ikea.iows+json;version=1.0',
#         'Consumer': 'MAMMUT',
#          })
# pdata = json.loads(rdata.data.decode('utf-8'))
#print(pdata["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])

while 1:
    text = irc.get_text()
    if text != bytes("", "UTF-8") :
       print(text)
    if bytes("PRIVMSG", "UTF-8") in text and bytes(channel, "utf-8") in text and ((bytes("!BLÅHAJ", "UTF-8") in text) or (bytes("!shark", "UTF-8") in text) or (bytes("!BLAHAJ", "UTF-8") in text) or (bytes("!🦈", "UTF-8")) in text ):
        rdata = http.request('GET',
                "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/30373588",
                headers={
                'Contract': '37249',
                'Accept': 'application/vnd.ikea.iows+json;version=1.0',
                'Consumer': 'MAMMUT',
                 })
        plain_data = json.loads(rdata.data.decode('utf-8'))
        irc.send(channel, "BLÅHAJ op vooraad in Ikea Delft: " + str(plain_data["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])+ " 🦈")
