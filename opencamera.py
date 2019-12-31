import cv2
import os
 
def generate():
    # path = os.path.abspath('E:/MySMP/haarcascades/haarcascade_frontalface_default.xml')
    path = os.path.abspath('haarcascades/haarcascade_frontalface_default.xml')
    print(path)
    face_cascade = cv2.CascadeClassifier(path)

    camera = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
 
        cv2.imshow("camera", frame)
        if cv2.waitKey(100) & 0xff == ord("q"):
            break
        elif count > 1:
            break
 
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate()