import  cv2
import numpy as np
import  time
import HPEModule  as hp

vCap = cv2.VideoCapture("videos/v3.mp4")
pDetector = hp.poseDetector()
while True:
    success, img = vCap.read()
    result, img = pDetector.getPose(img, True)
    landMarksList = pDetector.getPoseLandMarks(img, result,False)
    # print(landMarksList)
    lx = landMarksList[14][1]
    ly = landMarksList[14][2]
    cv2.circle(img, (lx, ly), 15, (255, 255, 255), cv2.FILLED)
    imS = cv2.resize(img, (960, 540))
    cv2.imshow("image", imS)
    cv2.waitKey(1)