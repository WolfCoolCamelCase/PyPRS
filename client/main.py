from config import *
import sys, socket
#Creating scoket
s = socket.socket()
#Checking correct parameters
try:
    s.connect((sys.argv[1], PORT))
except IndexError:
    print("Correct usage: python3 main.py [connection address]")
    raise SystemExit
#Connection loop
while 1:
    message = input(" -> ")
    if message == "exit":
        break
    s.send(message.encode())
    out = s.recv(1024).decode()
    print(out)
s.close()
