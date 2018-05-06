import cv2
import sys
import logging as log

from time import sleep

cascPath1 = 'face_detection2.xml'
faceCascade = cv2.CascadeClassifier(cascPath1)
anterior = 0

for i in range(51,101):
    frame=cv2.imread('D:\\vb Workz\\8th sem\\major proj2\\DATABASE\\Temp\\'+str(i+1)+'.jpg')
    print(frame)
    #frame=cv2.resize(frame,(480,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        
    )
    
    c=0
    for (x, y, w, h) in faces:
        c=c+1
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    crop_img = frame[y:y+h+10, x:x+w]
    crop_img=cv2.resize(crop_img,(128,128))

    #cv2.imshow('crop_img', crop_img)
    #cv2.imshow('image', frame)
    cv2.imwrite('D:\\vb Workz\\8th sem\\major proj2\\DATABASE\\'+str(i+1)+'.jpg',crop_img)
    
