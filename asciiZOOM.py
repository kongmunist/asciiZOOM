import cv2
from asciifyimage import asciify
import time
import threading
import socket
import sys


def listenThread():
    print("started listenin")
    while True:
        data, addr = sock.recvfrom(120000) # buffer size is 1024 bytes
        sys.stdout.flush()
        sys.stdout.write(data.decode('utf-8', 'ignore'))
        sys.stdout.write(imHolder[0])



UDP_IP = "unix8.andrew.cmu.edu"
UDP_PORT = 2323

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
imHolder = ["0"]

t = threading.Thread(target=listenThread, daemon=True)
t.start()
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    # sys.stdout.flush()
    # sys.stdout.write(asciify(frame))
    textImage = asciify(frame, 100)
    imHolder[0] = textImage
    sock.sendto(bytearray(textImage, 'utf8'),(UDP_IP, UDP_PORT))

    time.sleep(.05)

cap.release()
cv2.destroyAllWindows()



