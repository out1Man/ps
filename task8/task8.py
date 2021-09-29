import os
import cv2
vc=cv2.VideoCapture("C:\\Users\\out Man\\Desktop\\ps后端\\task8\\before.mp4")
c=1
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
while rval:
    rval,frame=vc.read()
    cv2.imwrite('C:\\Users\\out Man\\Desktop\\ps_png\\'+str(c)+'.png',frame)
    c=c+1
    cv2.waitKey(1)
vc.release()