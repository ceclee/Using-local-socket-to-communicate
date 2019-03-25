from socket import *
import os

address = './sockfile'
try:
    os.unlink(address)
except OSError:
    if os.path.exists(address):
        raise
s = socket(AF_UNIX,SOCK_STREAM)
s.bind(address)
s.listen(5)

while True:
    conn,addr = s.accept()
    print(addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('rec:',data)
        conn.send(b'good!!!')
    conn.close()
s.close()