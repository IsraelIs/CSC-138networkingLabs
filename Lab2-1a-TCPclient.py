#!/usr/bin/python
#TCP client, used for connection-oriented communication
from socket import *
serverName = 'localhost'
serverPort = 1337
#establishes connection with raw sockets to provide custom headers for the purposes of TCP
clientSocket = socket(AF_INET, SOCK_STREAM) # creates the socket using IPv4 and TCP
clientSocket.connect((serverName,serverPort)) #connect to remote socket using server name and port number.
sentence = raw_input('Input lowercase sentence:') #input string, will not display the actual text
clientSocket.send(sentence.encode()) #encode the sentence to UTF-8
modifiedSentence = clientSocket.recv(1024) #recieve data from buffer with max size of 1024, should be a power of 2
print('From Server: ' + modifiedSentence.decode())
clientSocket.close()
