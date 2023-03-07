from src.Camera import Camera 
from src.EmotionDetection import EmotionDetection

class Job:

    def __init__(self):

        self.camera = Camera()
        self.detector = EmotionDetection()
        

    def startCamera(self):

        self.camera.record = True
        self.camera.startRecording()
