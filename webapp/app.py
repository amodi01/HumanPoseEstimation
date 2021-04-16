from GymTrainerComponents.PoseDetector import PoseDetector
from flask import Flask, Response, render_template
import cv2
import  numpy as np
# app name
app = Flask(__name__)

# capture live video
video = cv2.VideoCapture(0)


# Home page
@app.route('/')
def index():
    return render_template('index.html')


# read video
def gen(video):
    pDetector = PoseDetector()
    count = 0
    direction = 0
    while True:
        success, img = video.read()
        # success, img = vCap.read()
        result, img = pDetector.getPose(img, True)
        landMarksList = pDetector.getPoseLandMarks(img, result, True)
        print(landMarksList)
        if len(landMarksList) != 0:
            angelR = pDetector.getAngle(img, 12, 14, 16, landMarksList)
            angelL = pDetector.getAngle(img, 11, 13, 15, landMarksList)
            # approximate range of angles 68-10, conver them between 0-100
            perR = np.interp(angelR, (150, 160), (0, 100))
            perL = np.interp(angelL, (130, 160), (0, 100))
            # print(angel)
            # print(per)
            if perL >= 90 and perL <= 100:
                color = (0, 255, 0)
                if direction == 0:
                    count += 0.5
                    direction = 1
            if perL >= 0 and perL <= 10:
                color = (0, 255, 0)
                if direction == 1:
                    count += 0.5
                    direction = 0

            if perR >= 90 and perR <= 100:
                color = (0, 255, 0)
                if direction == 0:
                    count += 0.5
                    direction = 1
            if perR >= 0 and perR <= 10:
                color = (0, 255, 0)
                if direction == 1:
                    count += 0.5
                    direction = 0
            print(count)
        text =  str(int(count))
        cv2.putText(img, text, (10, 500), cv2.FONT_HERSHEY_PLAIN, 10,
                    (255, 0, 0), 25)
        imS = cv2.resize(img, (1000, 600))
        cv2.imshow("image", imS)
        cv2.waitKey(1)

      #  ret, jpeg = cv2.imencode('.jpg', img)
        #frame = jpeg.tobytes()
       # yield (b'--frame\r\n'
          #     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    global video
    gen(video)
    #return Response(gen(video),
     #               mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
