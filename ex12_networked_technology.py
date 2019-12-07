# ex12_networked_technology.py

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )


# HTTP = HyperText Transfer Protocol
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


# using the Developer Console to Explore HTTP
# vývojář/Inspektor webu/síť/page1 - záhlaví/


