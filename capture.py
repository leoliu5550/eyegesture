import cv2 
import numpy as np

# cv2.rectangle(blank, (0,0), (250,250), (255,255,255), thickness = -1)
# cv2.imshow('Green', blank)
# cv2.waitKey(0)
# print(blank)

# get camera
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()

    # vis = img.copy()
    print(np.shape(img))
    cv2.rectangle(img, (0,0), (250,250), (0,255,0), thickness = 3)
    cv2.imshow('Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()