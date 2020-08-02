import keras
import cv2
import numpy as np
import matplotlib
import cv2
import numpy as np


# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 30, 60)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 240, 255, cv2.THRESH_BINARY_INV)

    return mask


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    ret1, frame1 = cap2.read()
    cv2.imshow('Original', (frame))
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# Release camera and close windows
cap.release()
cap2.release()
cv2.destroyAllWindows()