import cv2 as cv 

class Camera:

    def __init__(self):

        self.record = False


    def startRecording(self):

        if self.record == True:
            
            image = cv.VideoCapture(0)

            if image.isOpened():

                validate, frame = image.read()
               
                while validate:

                    validate, frame = image.read()
                    cv.imshow('Face Emotion Detection', frame)

                    key = cv.waitKey(5)
                    if key == 27:
                        break


            image.release()
            cv.destroyAllWindows()
        

