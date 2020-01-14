import socket
import sys


class IRC:

    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        print("PRIVMSG " + chan + " " + msg + "\r\n")
        self.irc.send(bytes("PRIVMSG " + chan + "\"" + msg + "\"" + "\r\n", "UTF-8"))

    def connect(self, server, channel, botnick):
        #defines the socket
        print("connecting to:"+server)
        self.irc.connect((server, 6667))                                                         #connects to the server
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!n\r\n", "UTF-8")) #user authentication
        self.irc.send(bytes("NICK " + botnick + "\r\n", "UTF-8"))               
        self.irc.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))

    def get_text(self):
        text=self.irc.recv(2040)  #receive the text
        return text
