import cv2
import mediapipe
import  math

class poseDetector():

    def __init__(self, mode=False, upperBody=False, smooth=True, detectConfidence=0.5, trackConfidence=0.5):
        self.Mode = mode
        self.UpperBody = upperBody
        self.Smooth = smooth
        self.DetectConfidence = detectConfidence
        self.TracKConfidence = trackConfidence
        self.MPdraw = mediapipe.python.solutions.drawing_utils
        self.MPpose = mediapipe.python.solutions.pose
        self.POSE = self.MPpose.Pose() #(self.Mode, self.Smooth, self.DetectConfidence, self.TracKConfidence)

    def getPose(self, img, draw=True):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.POSE.process(img)
        if results.pose_landmarks and draw:
            self.MPdraw.draw_landmarks(img, results.pose_landmarks, self.MPpose.POSE_CONNECTIONS)
        return results,img

    def getPoseLandMarks(self, img,results, draw=True):
        landMarksList=[]
        if results.pose_landmarks:
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landMarksList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 4, (0, 0, 255), cv2.FILLED)
        return  landMarksList

    def getAngle(self,img,p1,p2,p3,landMarkList,draw=True):
        p1_x,p1_y=landMarkList[p1][1:]
        p2_x, p2_y = landMarkList[p2][1:]
        p3_x, p3_y = landMarkList[p3][1:]

        angle=math.degrees(math.atan2(p3_y-p2_y,p3_x-p2_x) -math.atan2(p1_y-p2_y,p1_x-p2_x) )

        if draw:
            cv2.line(img,(p1_x,p1_y),(p2_x,p2_y),(255,255,255),3)
            cv2.line(img, (p3_x, p3_y), (p2_x, p2_y), (255, 255,255), 3)
            cv2.circle(img, (p1_x, p1_y), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (p1_x, p1_y), 35, (0, 0, 255), 2)
            cv2.circle(img, (p2_x, p2_y), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (p2_x, p2_y), 35, (0, 0, 255), 2)
            cv2.circle(img, (p3_x, p3_y), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (p3_x, p3_y), 35, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)),(p2_x -100,p2_y+100),cv2.FONT_HERSHEY_PLAIN,4,(255,255,0),4 )


def main():
    vCap = cv2.VideoCapture("videos/v1.mp4")
    pDetector = poseDetector()
    while True:
        success, img = vCap.read()
        result,img= pDetector.getPose(img, True)
        landMarksList=pDetector.getPoseLandMarks(img,result)
        #print(landMarksList)
        lx=landMarksList[14][1]
        ly=landMarksList[14][2]
        cv2.circle(img, (lx, ly), 15, (255, 255, 255), cv2.FILLED)
        imS = cv2.resize(img, (960, 540))
        cv2.imshow("image", imS)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
