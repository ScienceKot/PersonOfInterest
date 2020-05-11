import socket
import time
import json
import datetime
import cv2

#Initializarea procesului de facedetction
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

#Initializarea partii de networking

HOST = '127.0.0.1'
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

i = 0
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    '''''
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
    cv2.imshow("Video", frame)
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    data = {"Time" : datetime.datetime.now().strftime("%Y : %M : %d - %H : %m"), 'Faces' : len(faces)}
    data = json.dumps(data)
    data = data.encode()
    sock.send(data)
    time.sleep(2)
sock.close()