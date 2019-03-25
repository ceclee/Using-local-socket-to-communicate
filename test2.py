from socket import *
import time

address = './sockfile'

s = socket(AF_UNIX,SOCK_STREAM)
s.connect(address)
while True:
    a = input('input:')
    s.send(a.encode())
    p = time.time()
    data = s.recv(1024).decode()
    print(data)
    print(time.time() - p)
s.close()

# while True: 
#     s = socket(AF_UNIX,SOCK_STREAM)
#     s.connect(address)
#     a = input('input:')
#     s.send(a.encode())
#     p = time.time()
#     data = s.recv(1024).decode()
#     print(data)
#     s.close()
#     print(time.time() - p)


