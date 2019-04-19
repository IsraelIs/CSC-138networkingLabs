#!/usr/bin/python
#Simple SMTP client
from socket import *
import base64
import time
import os
import ssl
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

bytelength = 1024
email = input('email: ')
password = input('password: ')
to = input('send email to: ')
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)



# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = ssl.wrap_socket(socket(AF_INET, SOCK_STREAM)) #TCP connection
clientSocket.connect(mailserver)
clientSocket.starttls() #connect the Socket to the mailserver

recv = clientSocket.recv(bytelength).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(bytelength).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

base64_str = base64.b64encode(("\x00" + email + "\x00" + password).encode())
auth_msg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(auth_msg)
auth_recv = clientSocket.recv(bytelength).decode()
print(auth_recv)

email_from = "MAIL FROM:<" + email + ">\r\n"
clientSocket.send(email_from.encode())
from_recv = clientSocket.recv(bytelength).decode()
print(from_recv)
# Send RCPT TO command and print server response.
email_to = "RCPT TO:<" + to + ">\r\n"
clientSocket.send(email_to.encode())
to_recv = clientSocket.recv(bytelength)
to_recv = to_recv.decode()
print(to_recv)
# Send DATA command and print server response.
message = "DATA\r\n"
clientSocket.send(message.encode())
message_recv = clientSocket.recv(bytelength)
message_recv = message_recv.decode()
print(message_recv)
# Send message data.
subject = "Subject: Hello!\r\n\r\n"
clientSocket.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
clientSocket.send(date.encode())
# Message ends with a single period.
msg = "\r\n Hello There."
clientSocket.send(msg.encode())
clientSocket.send("\r\n.\r\n".encode())
msg_recv = clientSocket.recv(bytelength).decode()
print(msg_recv)
# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
quit_recv = clientSocket.recv(bytelength)
print(quit_recv.decode())
clientSocket.close()
