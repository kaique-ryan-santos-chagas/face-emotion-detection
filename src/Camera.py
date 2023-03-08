import cv2 as cv 
import time

from datetime import date 
from src.EmotionDetection import EmotionDetection

class Camera:

    def __init__(self):

        self.record = False
        self.detection = EmotionDetection()


    def startRecording(self):

        if self.record == True:
            
            image = cv.VideoCapture(0)

            videoName = date.today()

            imageWriter = cv.VideoWriter('videos/'+ str(videoName) +'.avi', cv.VideoWriter_fourcc(*'MJPG'), 30, (640,480))

            startTime = time.time()

            if image.isOpened():

                validate, frame = image.read()
               
                while validate:

                    validate, frame = image.read()
                    imageWriter.write(frame)
                    
                    if time.time() - startTime > 300: # 5 minutes in seconds 
                        break

            image.release()
            cv.destroyAllWindows()
        
