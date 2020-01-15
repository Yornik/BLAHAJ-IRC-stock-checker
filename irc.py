import socket
import sys
import time
import ssl

class IRC:

    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc = ssl.wrap_socket(self.irc, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="ECDHE-RSA-AES256-GCM-SHA384")

    def send(self, chan, msg):
        print("PRIVMSG " + chan + " " + msg + "\r\n")
        self.irc.send(bytes("PRIVMSG " + chan + " :" + msg + "\r\n", "UTF-8"))

    def connect(self, server, channel, botnick):
        #defines the socket
        print("connecting to:"+server)
        self.irc.connect((server, 6697))                                                         #connects to the server
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!n\r\n", "UTF-8")) #user authentication
        self.irc.send(bytes("NICK " + botnick + "\r\n", "UTF-8"))               
        self.irc.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))

    def get_text(self):
        text=self.irc.recv(4096)  #receive the text
        if text.find(bytes("PING", "utf-8"))!=-1:
           self.irc.send(bytes("PONG "+str(text.split()[1])+"\r\n", "UTF-8"))
           print("Pinged by the system")
        return text
