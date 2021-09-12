import socket

connected = True
s = socket.socket()

host="localhost"
port=7000

s.bind((host,port))
print('connected....')

s.listen(5)
print('listening to port ',port)

conn, address = s.accept()

while connected:
    conn.send(input("Message:").encode())
    
    message=conn.recv(2048)
    print(message.decode())