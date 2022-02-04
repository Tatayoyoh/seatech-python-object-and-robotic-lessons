from controller import Camera

class EpuckCamera(Camera):
    def __init__(self):
        super().__init__('camera')
        self.enable(samplingPeriod=50)
        self.recognitionEnable(samplingPeriod=100)
        self.__tracked_name = None

    def track_object(self, object_name):
        self.__tracked_name = object_name

    def is_tracked_object_present(self):
        objs = self.getRecognitionObjects()
        for obj in objs:
            if self.__tracked_name == obj.get_model().decode("utf-8"):
                self.__recognized_object = obj
                return True
        return False
        