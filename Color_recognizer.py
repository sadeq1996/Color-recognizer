import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #  range of blue color in HSV
    
    lower_color = np.array([175, 50, 50])
    upper_color = np.array([185, 255, 255])
    
    #?blue: low= ([110,50,50])| up= ([130,255,255])
    #^ yellow: low= ([15,50,50])| up= ([35,255,255])
    #!red: low= ([175,50,50])| up= ([185,255,255])
    
    # Threshold the HSV image to get only goal color
    mask = cv2.inRange(hsv, lower_color, upper_color)
  
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw a rectangle around color
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        if w*h > 1000: 
            cv2.rectangle(res,(x,y),(x+w,y+h),(0,165,255),2)
        

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) &0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()