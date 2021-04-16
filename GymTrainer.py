import  cv2
import numpy as np
from GymTrainerComponents import HPEModule as hp

vCap = cv2.VideoCapture("videos/v4.mp4")
pDetector = hp.PoseDetector()
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
    if per == 100:
        color = (0, 255, 0)
        if direction == 0:
            count += 0.5
            direction = 1
    if per == 0:
        color = (0, 255, 0)
        if direction == 1:
            count += 0.5
            direction = 0
    print(count)
    cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                (255, 0, 0), 25)
    imS = cv2.resize(img, (960, 540))
    cv2.imshow("image", imS)
    cv2.waitKey(1)