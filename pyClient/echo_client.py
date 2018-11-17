#!/usr/bin/env python3

import socket

HOST = '172.18.0.2'  #who we want to connect to
PORT = 65432  #specific port we want to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connect using the server ip and port
    s.sendall(b'HEllo world') #what we send to the server
    data = s.recv(1024)  #if server responds we put it in here

print('Received', repr(data))


