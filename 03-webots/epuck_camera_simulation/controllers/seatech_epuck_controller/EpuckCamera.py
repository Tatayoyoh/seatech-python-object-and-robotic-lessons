from controller import Camera

class EpuckCamera(Camera):
    def __init__(self, name):
        super().__init__(name)
        self.enable(samplingPeriod=50)
        self.recognitionEnable(samplingPeriod=100)