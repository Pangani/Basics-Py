import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 9999))

message = soc.recv(1024)
soc.close()

print(message.decode("ascii"))