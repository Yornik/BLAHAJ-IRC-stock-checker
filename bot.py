# YHeyl<yornik@yornik.nl> MIT liscense
# thanks to <mrngm> For help with the headers
## todo - YH
# - PEP 8
# - Bot should onlly be called if trigger words are the only message.
# - More parameters (difrent articels and stores/countries would be nice)
# - Docker file.
# - K8s Helm file.
# - More IKEA funtions. (opening times, price, location in pick up bay)
# - Pushing important events as a messege like a decrese or increse in stock.
# - Some nice help text.
# - Maybe in futere ordering via private messages.
# - Intregration with TRÅDFRI RGB bulb.
# - Running it in a lack rack.


from irc import *
import requests
import urllib3
import time
import json
import os
import random
http = urllib3.PoolManager()
channel ="##revspace-bot"
server = "irc.freenode.net"
nickname = "BLAHAJ_Delft_Bot"

irc = IRC()
irc.connect(server, channel, nickname)



while 1:
    text = irc.get_text()
    print(str(text))

    if bytes("PRIVMSG", "UTF-8") in text and bytes(channel, "utf-8") in text and ((bytes(":!ikea-art", "UTF-8") in text)):
        artnmr= str(text ,"UTF-8").split(":!ikea-art ")[1].split("\r\n'")[0].strip()
        print(artnmr+"end")
        titledata = http.request('GET',"https://www.ikea.com/nl/nl/p/n-" + artnmr)
        print(titledata.status)
        if titledata.status == 200:
            title = str(titledata.data , "UTF-8").split('<span class="product-pip__name" data-test-target-product-name>')[1].split('</span>')[0]
            desc = str(titledata.data , "UTF-8").split('<span class="normal-font range__text-rtl">')[1].split('</span>')[0]
            rdata = http.request('GET',
                "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/" + str(artnmr) ,
                headers={
                'Contract': '37249',
                'Accept': 'application/vnd.ikea.iows+json;version=1.0',
                'Consumer': 'MAMMUT',
                 })
            plain_data = json.loads(rdata.data.decode('utf-8'))
            irc.send(channel, str(text.split(bytes("!", "UTF-8"))[0])[3:-1] + ": De hoeveelheid " + title  + " bij de IKEA vestiging delft is " + str(plain_data["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"]) + " de artikel beschrijving is als volgt: " + desc.strip() )
    if bytes("PRIVMSG", "UTF-8") in text and bytes(channel, "utf-8") in text and ((bytes(":!BLÅHAJ\r\n", "UTF-8") in text) or (bytes(":!shark\r\n", "UTF-8") in text) or (bytes(":!BLAHAJ\r\n", "UTF-8") in text) or (bytes(":!🦈\r\n", "UTF-8")) in text ):
        rdata = http.request('GET',
                "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/30373588",
                headers={
                'Contract': '37249',
                'Accept': 'application/vnd.ikea.iows+json;version=1.0',
                'Consumer': 'MAMMUT',
                 })
        plain_data = json.loads(rdata.data.decode('utf-8'))
        irc.send(channel, str(text.split(bytes("!", "UTF-8"))[0])[3:-1] + ": De hoeveelheid BLÅHAJ`s op dit moment bij de IKEA vestiging delft is " + str(plain_data["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])+ " 🦈")

    if bytes("PRIVMSG", "UTF-8") in text and bytes(channel, "utf-8") in text and ((bytes(":!babyBLÅHAJ\r\n", "UTF-8") in text) or (bytes(":!babyshark\r\n", "UTF-8") in text) or (bytes(":!babyBLAHAJ\r\n", "UTF-8") in text) or (bytes(":!baby🦈\r\n", "UTF-8")) in text ):
        rdata = http.request('GET',
                "https://iows.ikea.com/retail/iows/nl/nl/stores/151/availability/ART/50455234",
                headers={
                'Contract': '37249',
                'Accept': 'application/vnd.ikea.iows+json;version=1.0',
                'Consumer': 'MAMMUT',
                 })
        plain_data = json.loads(rdata.data.decode('utf-8'))
        irc.send(channel, str(text.split(bytes("!", "UTF-8"))[0])[3:-1] + ": De hoeveelheid baby BLÅHAJ`s op dit moment bij de IKEA vestiging delft is " + str(plain_data["StockAvailability"]["RetailItemAvailability"]["AvailableStock"]["$"])+ " 🦈")

