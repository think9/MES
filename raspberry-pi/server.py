import cv2
import os

cap = cv2.VideoCapture(0)
count = 440
print "Video caputre start.."

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print "No frame"
        break
    count += 1
    if count == 450:
        print "Send frame to the server"
        cv2.imwrite("frame.png", frame)
        os.system("scp -i hyssug.pem frame.png ubuntu@13.209.75.104:/home/ubuntu/img")
        os.remove("frame.png")
        count = 0
        print "Send complete!"

cap.release()
