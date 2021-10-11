import socket
s = socket.socket()
host = socket.gethostname()
port = 8080 

s.bind((host,port))
s.listen(5)
print(host)
print("Waiting for any incoming connections ...") 

conn,addr=s.accept()
print(addr,"Has connected to the server")

filename=input(str("please enter the filename of the file : "))
file=open(filename,'rb')
file_data=file.read(1024)
conn.send(file_data)
print("file has been transmitted successfully")
