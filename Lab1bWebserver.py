from socket import *
import sys 
serverSocket = socket(AF_INET, SOCK_STREAM)#tcp protocol SOCK_STREAM, UDP is SOCK_DGRAM socket types AF_INET designates IPV4
serverPort = 9001 #port listened on
serverSocket.bind(('',serverPort)) #binds server socket to Address of local host and PORT locahost:9001, cannot already be bound
serverSocket.listen(1) #listens to amount of queued connections
#Prepare a sever socket
while True:
 #Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept() #accepts the connection bound to the address from serverSocket.bind 
 #Fill in start #Fill in end
	try:
		message = connectionSocket.recv(1024)  #recieves data from socket in 1024 bytes
		print message.split()
		filename = message.split()[1]
		f = open(filename[1:],'rb') #openfile and readbinary for nonhuman code(images)
		outputdata = 'HTTP/1.1 200 OK\r\n\r\n'
		outputdata = outputdata + f.read() #read from file
	
 #Send one HTTP header line into socket
 #Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i]) #sends the split message from outputdata
		connectionSocket.send("\r\n")#sends data to connected socket

		connectionSocket.close()
	except IOError as e:
	#Send response message for file not found
		outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		connectionSocket.close()
	except IndexError as e: #has index error and gets angry at favicon.io file if error not caught
		print 'index error'
		connectionSocket.close()
serverSocket.close()# close server socket
sys.exit()#Terminate the program after sending the corresponding data 