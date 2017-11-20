import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
size = (256, 144)

while True:
    _, frame = cap.read()
    frame = cv2.resize(fram     e, size)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 92, 120])
    upper_yellow = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    blur_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    median_frame = cv2.medianBlur(frame, 15)

    cv2.imshow('frame', frame)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('no smoothing analysis result', res)
    cv2.imshow('with gaussian blur', blur)
    cv2.imshow('with median blur', median)
    cv2.imshow('with bilateral blur', bilateral)
    cv2.imshow('original frame with median blur', median_frame)
    cv2.imshow('original frame with gaussian blur', blur_frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
