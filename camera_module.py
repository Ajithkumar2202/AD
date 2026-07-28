


import cv2

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    if ret:
        cv2.imwrite("accident.jpg", frame)
        print("Image Captured")

    cam.release()