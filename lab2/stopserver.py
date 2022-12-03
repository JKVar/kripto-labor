import socket

host = '0.0.0.0'
port = 2001
s = socket.socket()
s.connect((host, port))

leallit = 'stop'
s.send(leallit.encode())
