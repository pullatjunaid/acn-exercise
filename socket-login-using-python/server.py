import socket
import os
import threading
import hashlib
import mysql.connector

# Create Socket (TCP) Connection
ServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1235
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
HashTable = {}


def threaded_client(connection):
    connection.send(str.encode('ENTER USERNAME : '))
    name = connection.recv(2048)
    connection.send(str.encode('ENTER PASSWORD : '))
    password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    # password = hashlib.sha256(str.encode(password)).hexdigest()

    # REGISTERATION PHASE

    try:
        mydb = mysql.connector.connect(host="localhost",
                                       username="newuser",
                                       password="password",
                                       database="acn")
    except mysql.connector.Error as err:
        print("Database connection failed", err)
        exit()

    # If new user,  regiter in Hashtable Dictionary
    cursor = mydb.cursor()
    cursor.execute("select * from authusers")
    result = cursor.fetchall()
    print(result)
    userExists = False
    userData = ""
    for user in result:
        if user[1] == name:
            userExists = True
            userData = user

    if userExists:
        # USER EXISTS, LOGIN USER
        print('\n', type(userData[2]), type(password))
        if userData[2] == password:
            connection.send(str.encode('Connection Successful'))
            print('Connected : ', name)
        else:
            connection.send(
                str.encode('Login Failed, Username or password is incorrect!'))
            print('Connection denied : ', name)
    else:
        # REGISTER NEW USER
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO authusers (username, password) values('" +
                       name + "','" + password + "')")

        connection.send(
            str.encode('Registeration Successful with usrname: ' + name))
    exit()

while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(target=threaded_client, args=(Client, ))
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()