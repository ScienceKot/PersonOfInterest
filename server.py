# Importarea bibliotecilor necesare
import socket
import json
#Setarea hostului și portului (pentur localhost în cazul dat)
HOST = '127.0.0.1'
PORT = 8000
#Inițializarea conecțiunii
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
# Conectarea la client
conn, addr = sock.accept()
print("Connected by: {}".format(addr))
while True:
    # Receptionarea datelor de la client
    data = conn.recv(1024)
    if data == None:
        continue
    else:
        # Convertirea datelor cu format byte în format string
        data = data.decode('utf-8')
        # Convertirea din string în dictionar
        data = json.loads(data)
        print(data)
# Închiderea conecțiunii
conn.close()
sock.close()
