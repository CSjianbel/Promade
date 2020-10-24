import time
import cv2

video = cv2.VideoCapture(0)
"face detector"
face_cascade = cv2.CascadeClassifier("../venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")
# face_cascade = cv2.CascadeClassifier("../venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
"eye detector"
# face_cascade = cv2.CascadeClassifier("../venv/lib/python3.8/site-packages/cv2/data/haarcascade_lefteye_2splits.xml")


frames = 0

while True:

    frames += 1
 
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Capturing", frame)

    if cv2.waitKey(1) == ord('q'):
        break

print("Frames:", frames)