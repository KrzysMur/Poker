import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 4321))

msg = s.recv(256)
print(msg.decode("utf-8"))
