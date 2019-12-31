# coding: utf-8
import cv2
import os
 
def generate():

    # 载入算法
    face_cascade = cv2.CascadeClassifier(os.path.abspath('haarcascades/haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.abspath('haarcascades/haarcascade_eye.xml'))

    # 获取摄像头
    camera = cv2.VideoCapture(0)

    # 人脸统计
    count = 0

    while (True):
        # 读取摄像头 (ret是布尔值, frame就是每一帧的图像)
        ret, frame = camera.read()
        
        # 二值化灰度处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None)
            # image : 二值化后的数据
            # scaleFactor : 表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
            # minNeighbors : 表示构成检测目标的相邻矩形的最小个数(默认为3个)。
        faces = face_cascade.detectMultiScale(gray, 1.3, 10)
        for (x,y,w,h) in faces:
            # rectangle()这个函数的作用是在图像上绘制一个简单的矩形。
                # img, pt1, pt2, color, thickness=None, lineType=None, shift=None
                # frame(图像)
                # pt1 框型左上点
                # pt2 框型右下点
                # color RGB色彩 框型色彩
                # thickness 框的厚度 如果是-1则填充整个矩形
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
 
        cv2.imshow("camera", frame)
        # cv2.imshow('peilpo', f)
        if cv2.waitKey(100) & 0xff == ord("q"):
            break
        elif count > 1:
            break
 
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate()