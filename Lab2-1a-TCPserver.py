#!/usr/bin/python
from socket import *
serverPort = 1337
serverSocket = socket(AF_INET,SOCK_STREAM) #establish tcp connection
serverSocket.bind(('',serverPort))#bind to port
serverSocket.listen(1)
print 'The server is ready to receive'
while True: #once the message is recieved convert to uppercase text
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()