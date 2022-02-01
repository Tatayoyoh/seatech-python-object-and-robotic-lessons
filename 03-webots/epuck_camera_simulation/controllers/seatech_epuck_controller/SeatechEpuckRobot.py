from controller import Robot, DistanceSensor
from EpuckMotors import EpuckMotors
from EpuckCamera import EpuckCamera
from EpuckDistanceSensors import EpuckDistanceSensors


class SeatechEpuckRobot(Robot):

    def __init__(self, speed=None):
        super().__init__()
        self.__motors = EpuckMotors()
        self.__camera = EpuckCamera('camera')
        self.__distance_sensors = EpuckDistanceSensors()
        # self.__camera. TODO set Recognition Nodes into World
        
            
        self.__speed = speed
        if speed is None:
            self.__speed = self.__motors.get_max_speed()

    def run(self, backward=False, left=False, right=False):
        speed = (-self.__speed) if backward == True else self.__speed
        self.__motors.run(speed=speed, left=left, right=right)

        if self.__distance_sensors.front_right_collision_detected():
            self.__motors.turn_left()
        if self.__distance_sensors.front_left_collision_detected():
            self.__motors.turn_right()

    def stop(self, backward=False):
        self.__motors.run(speed=0)

    def turn_left(self):
        self.__motors.turn_left()

    def turn_right(self):
        self.__motors.turn_right()

    def get_recognized_objects(self):
        print(self.__camera.getRecognitionNumberOfObjects())
        return self.__camera.getRecognitionObjects()
