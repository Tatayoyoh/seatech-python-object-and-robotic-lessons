import re
from heritage import FieldTypeRobot
from heritage import GroundRobot, AirRobot, SurfaceRobot, UnderseaRobot

class RobotFactory():
    @staticmethod
    def create(robot_type, name):
        if robot_type == 'ground':
            return GroundRobot(name)
        elif robot_type == 'air':
            return AirRobot(name)
        elif robot_type == 'surface':
            return SurfaceRobot(name)
        elif robot_type == 'undersea':
            return UnderseaRobot(name)
        else:
            print('bad robot type')
            return None

if __name__ == '__main__':

    robot = RobotFactory.create('air', 'Super Copter')
    robot.status()
    robot = RobotFactory.create('ground', 'Heavy Raptor')
    robot.status()
    robot = RobotFactory.create('surface', 'Hydro Speeder')
    robot.status()
    robot = RobotFactory.create('undersea', 'Silent Nautilus')
    robot.status()
