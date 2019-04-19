#!/usr/bin/python
#UDP is connection-less, so the client automatically recieves a response from the server without a response
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input('input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
newMessage,serverAddress=clientSocket.recvfrom(2048)
print newMessage.decode()
clientSocket.close()
