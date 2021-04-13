import cv2
import mediapipe


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
