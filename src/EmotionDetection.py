import cv2 as cv

from fer import FER, Video
from datetime import time

class EmotionDetection:

    def __init__(self):

        date = date.today()

        self.detector = FER(mtcnn=True)
        self.video = Video('videos/'+ str(date))


    def startDetection(self):

        rawData = self.video.analyze(self.detector, display=True)
        


