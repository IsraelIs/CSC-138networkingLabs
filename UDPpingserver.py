import random
from socket import *

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',12000))

while True:
		rand = random.randint(1,10)
		message,address = serverSocket.recvfrom(1024)
		print message
		message=message.upper()
		
		if rand<4:
			print 'packet dropped'
			continue
		serverSocket.sendto(message,address)