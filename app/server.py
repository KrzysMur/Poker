import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4321))
s.listen(5)


while True:
    client_socket, address = s.accept()
    print(f"Connection with {address} established.")
    client_socket.send(bytes("Connected to server", "utf-8"))
