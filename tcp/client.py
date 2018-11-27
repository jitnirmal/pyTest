import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('sending data')
s.connect(('localhost', 50000))
s.sendall('client 1')
data = s.recv(1024)
s.close()
print ('Received', data)
