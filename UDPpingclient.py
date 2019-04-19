import time
from socket import *
import datetime

for pings in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    message = 'ping'
    addr = ("localhost", 12000)

    start = datetime.datetime.now()
    clientSocket.sendto(message, addr)
    try:
        data, server = clientSocket.recvfrom(1024)
        end = datetime.datetime.now()
        elapsed = end - start
        print '{0} {1} {2}'.format(data, pings, elapsed.total_seconds())
    except timeout:
        print 'Request timed out'
	clientSocket.close()
	