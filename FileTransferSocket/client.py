import socket # Import socket module
s = socket.socket() # Create a socket object
host = input(str("please enter the host address of the sender : "))
port = 8080
s.connect((host,port))
print("connected...")
filename=input(str("please enter a filename for the incoming file : "))
file=open(filename,'wb')
file_data=s.recv(1024)
file.write(file_data)
file.close()
print("file has been received successfully")