import cv2
import os

# pip install opencv-python==4.5.2

video=cv2.VideoCapture(0)


facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

name_list = [ " ", "Prabhas", "Mridul", "Priyal"]

imgBackground = cv2.imread("background.jpg")



while True:
    ret, frame = video.read()
    if not ret:
        print("Error reading video feed")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        print("Recognized:", name_list[serial], "Confidence:", conf)
        if conf > 50:
            cv2.putText(frame, name_list[serial], (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        else:
            cv2.putText(frame, "Recognized", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
print("Dataset collection Done.................")