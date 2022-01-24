from polymorphism import Robot
from polymorphism import UnmannedVehicle
from polymorphism import UnmannedUnderwaterVehicle

class RobotFactory():

    @staticmethod
    def create_simple_robot():
        return Robot()

    @staticmethod
    def create_unmanned_robot():
        return UnmannedVehicle()

    @staticmethod
    def create_undersea_robot():
        return UnmannedUnderwaterVehicle()

if __name__ == '__main__':

    factory = RobotFactory()

    robot = RobotFactory.create_simple_robot()
    robot.start_mission()

    robot = RobotFactory.create_unmanned_robot()
    robot.start_mission('mission1')

    robot = RobotFactory.create_undersea_robot()
    robot.start_mission('mission2')        