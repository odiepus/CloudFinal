#!/usr/bin/env python3

import socket

HOST = '172.18.0.2' #this ip to listen on
PORT = 65432        #port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  #bind the port and ip addr to this socket object
    s.listen()              #listen on port and ip addr
    conn, addr = s.accept()  #if pinged for connection then grab the pingers connection info and addr

    with conn:
        print ("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
