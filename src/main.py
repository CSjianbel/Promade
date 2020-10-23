import os
import cv2

# Reads the image as a numpy array
img = cv2.imread(os.path.join("images/", "test.png"), 1)

face_cascade = cv2.CascadeClassifier("../venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Creates a window that shows the image
cv2.imshow("(G)I-DLE", img)

# Window stays open given the argument [0 by default waits for a key to be pressed]
cv2.waitKey(0)

# Destroys all windows open
cv2.destroyAllWindows()
