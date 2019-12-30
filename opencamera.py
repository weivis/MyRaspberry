# -*- coding: UTF-8 -*-
import cv2
#引入库
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
#读取内容
    if cv2.waitKey(10) == ord("q"):
        break
        
#随时准备按q退出
cap.release()
cv2.destroyAllWindows()
