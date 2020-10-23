import time
import cv2

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("../venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")

frames = 0

while True:

    frames += 1

    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("Frames:", frames)