import socket
import mysql.connector

mydb = ""


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Starting Server...")

try:
    mydb = mysql.connector.connect(host="localhost",
                                   user="newuser",
                                   password="password",
                                   database="dns")
    print("Database connected successfully...\n")

except mysql.connector.Error as err:
    print("Database connection error", err)
    exit()

s.bind(("127.0.0.1", 1234))


def getFromDb(data, address):
    dbcursor = mydb.cursor()
    dbcursor.execute("select * from dnslist where domain='" + data + "'")
    result = dbcursor.fetchall()
    if len(result) > 0:
        for row in result:
            ip = row[2]
            send = s.sendto(ip.encode(), address)
    else:
        # print('Ip address not found...')
        send = s.sendto(("IP address not found").encode(), address)

while True:
    data, address = s.recvfrom(1024)
    print(f"{address} wants to fetch data!")
    data = data.decode()
    getFromDb(data, address)
    # ip = dns_table.get(data, "Not Found!").encode()
    # send = s.sendto(ip, address)
    # s.close()
