import socket 

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(("127.0.0.1", 9999))

soc.listen()

print("Server is listening...")

while True:
    client, address = soc.accept()
    print(f"Connected to {address}.")
    
    message = "Welcome to the server!"
    client.send(message.encode("ascii"))
    client.close()