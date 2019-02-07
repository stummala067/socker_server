#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.222.33.53'
print(host)
port = 12221
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print('[Waiting for connection...]')
       c, addr = s.accept()
       print('Got connection from', addr)
   else:
       # Halts
       print('[Waiting for response...]')
       print(c.recv(1024))
       q = raw_input("Enter something to this client: ")
       c.send(q)
