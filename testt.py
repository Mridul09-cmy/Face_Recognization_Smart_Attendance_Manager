import cv2
import os
import csv
import numpy as np
from datetime import datetime

# Load the trained LBPHFaceRecognizer model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

# Load the face cascade classifier
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# List of names corresponding to IDs in the trained model
name_list = [" ", "Mridul", "Tiwari", "Mustafa" ]  # Update with your actual names

# Function to update attendance in CSV file
def update_attendance(name, filename):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_time])

# Video capture from default webcam
video = cv2.VideoCapture(0)

# Main loop for face recognition and attendance updating
while True:
    ret, frame = video.read()
    if not ret:
        print("Error reading video feed")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Crop face region of interest (ROI)
        face_roi = gray[y:y+h, x:x+w]

        # Perform recognition on the face ROI
        serial, confidence = recognizer.predict(face_roi)

        # Get the recognized name
        recognized_name = name_list[serial]

        # Print recognition details for debugging
        print("Recognized:", recognized_name, "Confidence:", confidence)

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # If the confidence is below a certain threshold, update attendance and display name
        if confidence < 70:
            # Update attendance
            update_attendance(recognized_name, "attendance.csv")
            # Display name
            cv2.putText(frame, recognized_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        else:
            # If confidence is too low, label as Unknown
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()
print("Attendance updated and program terminated.")
