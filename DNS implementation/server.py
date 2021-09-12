import socket


dns_table = {"github.com": "207.97.227.239",
             "reddit.com": "72.247.244.88",
             "www.youtube.com":"142.250.67.46",
             "www.google.com":"142.250.183.228",
             }
             
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Starting Server...")
s.bind(("127.0.0.1",1234))

while True:
    data, address = s.recvfrom(1024)
    print(f"{address} wants to fetch data!")
    data = data.decode()
    ip = dns_table.get(data, "Not Found!").encode()
    send = s.sendto(ip,address)
    # s.close()
