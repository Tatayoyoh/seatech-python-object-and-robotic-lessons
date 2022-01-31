from controller import Robot, Motor
from EpuckMotors import EpuckMotors

class SeatechEpuckRobot(Robot):

    def __init__(self, speed=None):
        super().__init__()
        self.__motors = EpuckMotors()
        self.__speed = speed
        if speed is None:
            self.__speed = self.__motors.get_max_speed()

    def run(self, backward=False, left=False, right=False):
        speed = (-self.__speed) if backward == True else self.__speed
        self.__motors.run(speed=speed, left=left, right=right)

    def stop(self, backward=False):
        self.__motors.run(speed=0)

    def turn_left(self):
        self.__motors.turn_left()

    def turn_right(self):
        self.__motors.turn_right()
