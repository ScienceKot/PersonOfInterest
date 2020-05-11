import socket
import json

HOST = '127.0.0.1'
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

conn, addr = sock.accept()
print("Connected by: {}".format(addr))
while True:
    data = conn.recv(1024)
    if data == None:
        continue
    else:
        data = data.decode('utf-8')
        data = json.loads(data)
        print(data)
conn.close()
sock.close()