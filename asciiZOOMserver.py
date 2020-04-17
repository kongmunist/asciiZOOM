##### Server
import socket
import threading
import time

def thr_rec(ad1, ad2):
    print("started listening")
    print(ad1)
    print(ad2)
    print("~~~~~")
    while True:
        data, addr = sock.recvfrom(120000) # buffer size is 1024 bytes
        if (addr == ad1):
            sock.sendto(data, ad2)
        else:
            sock.sendto(data, ad1)
            
        #print(data, addr)

#UDP_IP = "127.0.0.1"
UDP_IP = "unix8.andrew.cmu.edu"
UDP_PORT = 2323

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
data2, addr2 = sock.recvfrom(1024)

while (addr[0] == addr2[0]):
    data2, addr2 = sock.recvfrom(1024)

print("start addresses")
print(addr)
print(addr2)
print("end addresses")
t = threading.Thread(target=thr_rec, args=[addr, addr2])
t.start()

while True:
    pass
