import cv2
#import mediapipe as mp
#import  time
import mediapipe
#import mediapipe.python as mp

mpDraw=mediapipe.python.solutions.drawing_utils
mpPose = mediapipe.python.solutions.pose
pose=mpPose.Pose()

vCap = cv2.VideoCapture("videos/v2.mp4")

#prevTime=0
while True:
    success, img= vCap.read()
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx,cy= int( lm.x * w), int(lm.y* h)
            cv2.circle(img,(cx,cy),4,(0,0,255),cv2.FILLED)
            print(id,lm)
    imS = cv2.resize(img, (960, 540))
    cv2.imshow("image",imS)
    cv2.waitKey(1)