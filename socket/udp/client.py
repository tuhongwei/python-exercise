import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = [b'Michael', b'Tracy', b'Sarah']
for d in data:
	s.sendto(d,('127.0.0.1',9999))
	print(s.recv(1024).decode('utf-8'))
s.close()