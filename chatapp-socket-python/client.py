import socket
PORT = 7000
FORMAT = 'utf-8'
connected = True
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "localhost"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
name = input("Enter user name: ")
client.send(name.encode(FORMAT))
server = client.recv(2048).decode(FORMAT)
print("[CONNECTED]" ,server, " has joined....")
while connected:
    message = (client.recv(2048)).decode(FORMAT)
    print(server,": ",message)
    message = input("My msg: ")
    client.send(message.encode(FORMAT))
    if (message == DISCONNECT_MESSAGE):
        connected = False