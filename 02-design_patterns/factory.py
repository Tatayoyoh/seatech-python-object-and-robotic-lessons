import sys
import time


class UnmannedRobot():
    __mission_running = False
    __mission = None

    @property
    def mission(self):
        return self.__mission

    @property
    def mission_running(self):
        return self.__mission_running

    def _write_message(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(1)

    # private
    def __safety_checks(self):
        self._write_message('Code safety checks... ')
        self._write_message('OK\n')
        self._write_message('Mecanic safety checks... ')
        self._write_message('OK\n')
        self._write_message('Electronic safety checks... ')
        self._write_message('OK\n')

    # private
    def __integrity_checks(self):
        self._write_message('Mission data integrity checks... ')
        self._write_message('OK\n')
        self._write_message('Mecanic integrity checks... ')
        self._write_message('OK\n')
        self._write_message('Electronic integrity checks... ')
        self._write_message('OK\n')

    # private
    def __plan_mission(self, mission):
        if type(mission) is not str: # some weah checks...
            print('Mission format is not valid')
            return False
        self.__mission = mission
        print('Recorded mission is validated and saved')
        return True

    # private
    def __run_mission(self):
        self.__mission_running = True
        print('Mission %s is running'%(self.__mission))

    # public
    def start_mission(self, mission):
        self.__safety_checks()
        if self.__plan_mission(mission):
            self.__run_mission()

    # public
    def stop_mission(self):
        self.__mission_running = False
        print('Mission %s was stopped'%(self.__mission))
        self.__integrity_checks()

class FieldTypeRobot(UnmannedRobot):
    __field = None

    def __init__(self, field):
        self.__field = field
        super().__init__()

    @property
    def field(self):
        return self.__field

class GroundRobot(FieldTypeRobot):

    def __init__(self):
        super().__init__('ground')

    # public
    def start_mission(self, mission):
        self.__safety_checks()
        if self.__plan_mission(mission):
            self.__run_mission()

    # public
    def stop_mission(self):
        self.__mission_running = False
        print('Mission %s was stopped'%(self.__mission))
        self.__integrity_checks()

class AirRobot(FieldTypeRobot):

    def __init__(self):
        super().__init__('air')

    # public
    def start_mission(self, mission):
        self.__safety_checks()
        if self.__plan_mission(mission):
            self.__run_mission()

    # public
    def stop_mission(self):
        self.__mission_running = False
        print('Mission %s was stopped'%(self.__mission))
        self.__integrity_checks()

class UnderseaRobot(FieldTypeRobot):

    def __init__(self):
        super().__init__('undersea')

    # public
    def start_mission(self, mission):
        self.__safety_checks()
        if self.__plan_mission(mission):
            self.__run_mission()

    # public
    def stop_mission(self):
        self.__mission_running = False
        print('Mission %s was stopped'%(self.__mission))
        self.__integrity_checks()

class SurfaceRobot(FieldTypeRobot):

    def __init__(self):
        super().__init__('surface')

    # public
    def start_mission(self, mission):
        self.__safety_checks()
        if self.__plan_mission(mission):
            self.__run_mission()

    # public
    def stop_mission(self):
        self.__mission_running = False
        print('Mission %s was stopped'%(self.__mission))
        self.__integrity_checks()

class RobotFactory():
    @staticmethod
    def create(robot_type):
        if robot_type == 'ground':
            return GroundRobot()
        elif robot_type == 'air':
            return AirRobot()
        elif robot_type == 'surface':
            return SurfaceRobot()
        elif robot_type == 'undersea':
            return UnderseaRobot()
        else:
            print('bad robot type')
            return None

if __name__ == '__main__':

    robot = UnmannedRobot()
    robot.start_mission('Go to the moooon')
    robot.stop_mission()

    robot = RobotFactory.create('air')
    robot.status()
    robot = RobotFactory.create('ground')
    robot.status()
    robot = RobotFactory.create('surface')
    robot.status()
    robot = RobotFactory.create('undersea')
    robot.status()
