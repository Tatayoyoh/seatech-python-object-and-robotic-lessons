from time import time
from controller import Robot, DistanceSensor
from EpuckMotors import EpuckMotors
from EpuckCamera import EpuckCamera
from EpuckDistanceSensors import EpuckDistanceSensors


class SeatechEpuckRobot(Robot):

    def __init__(self, speed=None, sampling_period=1):
        super().__init__()
        self.__motors = EpuckMotors()
        self.__camera = EpuckCamera()
        self.__distance_sensors = EpuckDistanceSensors()
        self.__goal_reached = False
        self.__sampling_period = sampling_period

        self.__speed = speed
        if speed is None:
            self.__speed = self.__motors.get_max_speed()

    @property
    def goal_reached(self):
        return self.__goal_reached

    def track_object(self, object_name):
        self.__camera.track_object(object_name)

    def __process_recognition(self):

        # if self.__camera.is_tracked_object_on_left():
        #     self.turn_left(capacity=0.5)
        # if self.__camera.is_tracked_object_on_right():
        #     self.turn_right(capacity=0.5)
        if self.__camera.is_tracked_object_present():
            self.__goal_reached = True

    def run(self, backward=False, left=False, right=False):
        speed = (-self.__speed) if backward == True else self.__speed
        self.__motors.run(speed=speed, left=left, right=right)

        # process recognition every X steps
        if round(self.getTime() % self.__sampling_period , 1) == 0.1:
            self.__process_recognition()

        if self.__distance_sensors.front_right_collision_detected():
            self.turn_left()
        elif self.__distance_sensors.front_left_collision_detected():
            self.turn_right()

    def stop(self, backward=False):
        self.__motors.run(speed=0)

    def turn_left(self, capacity=1):
        self.__motors.turn_left(capacity=capacity)

    def turn_right(self, capacity=1):
        self.__motors.turn_right(capacity=capacity)
