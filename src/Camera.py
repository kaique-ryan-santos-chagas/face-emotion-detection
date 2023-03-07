import cv2 as cv 
import time

class Camera:

    def __init__(self):

        self.record = False


    def startRecording(self):

        if self.record == True:
            
            image = cv.VideoCapture(0)
            imageWriter = cv.VideoWriter('videos/output.avi', cv.VideoWriter_fourcc(*'MJPG'), 30, (640,480))

            if image.isOpened():

                validate, frame = image.read()
               
                while validate:

                    validate, frame = image.read()
                    imageWriter.write(frame)


            image.release()
            cv.destroyAllWindows()
        

