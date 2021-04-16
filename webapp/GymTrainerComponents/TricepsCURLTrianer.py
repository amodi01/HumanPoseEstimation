import  cv2
import numpy as np
from webapp.GymTrainerComponents.PoseDetector import PoseDetector

vCap = cv2.VideoCapture("videos/v4.mp4")
pDetector = PoseDetector()
count = 0
direction = 0
while True:
    success, img = vCap.read()
    result, img = pDetector.getPose(img, False)
    landMarksList = pDetector.getPoseLandMarks(img, result,False)
    angel=pDetector.getAngle(img,12,14,16,landMarksList)
    #angel= pDetector.getAngle(img, 11, 13, 15, landMarksList)
    #approximate range of angles 68-10, conver them between 0-100
    per=np.interp(angel,(65,155),(0,100))
    print(angel)
    print(per)
    if per >= 90 and per <= 100:
        color = (0, 255, 0)
        if direction == 0:
            count += 0.5
            direction = 1
    if per >= 0 and per <= 10:
        color = (0, 255, 0)
        if direction == 1:
            count += 0.5
            direction = 0
    print(count)
    text= "Triceps Reps Count : " + str(int(count))
    cv2.putText(img, text, (45, 670), cv2.FONT_HERSHEY_PLAIN, 10,
                (255, 0, 0), 25)
    imS = cv2.resize(img, (1600, 1000))
    cv2.imshow("image", imS)
    cv2.waitKey(1)