from abc import ABCMeta, abstractmethod, abstractproperty 

class UnmannedRobot(metaclass=ABCMeta):
    @abstractproperty
    def mission(self):
        pass

    @property
    def mission_running(self):
        return self.__mission_running
    
    @abstractmethod
    def start_mission(self):
        pass

    @abstractmethod
    def stop_mission(self):
        pass

class FieldTypeUnmannedRobot(UnmannedRobot):
    __field = None
    mission = None

    def __init__(self, field):
        self.__field = field
        # super().__init__()  # abstract parent, __init__ call is not needed

    @property
    def field(self):
        return self.__field

class GroundRobot(FieldTypeUnmannedRobot):

    def __init__(self):
        super().__init__('ground')

    def start_mission(self):
        print("%s: Let's have a ride !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class AirRobot(FieldTypeUnmannedRobot):
    # mission = None

    def __init__(self):
        FieldTypeUnmannedRobot.__init__(self, 'air')

    def start_mission(self):
        print("%s: Let's liftoff in the air !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class UnderseaRobot(FieldTypeUnmannedRobot):

    def __init__(self):
        super().__init__('undersea')

    def start_mission(self):
        print("%s: Let's dive captain !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class SurfaceRobot(FieldTypeUnmannedRobot):

    def __init__(self):
        super().__init__('surface')

    def start_mission(self):
        print("%s: Let's slide on the sea !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class RobotFactory():
    @staticmethod
    def create_air_robot():
        return AirRobot()

    @staticmethod
    def create_ground_robot():
        return GroundRobot()

    @staticmethod
    def create_surface_robot():
        return SurfaceRobot()

    @staticmethod
    def create_undersea_robot():
        return UnderseaRobot()

if __name__ == '__main__':

    print("We will play with 'start_mission' and 'stop_mission' from child objects of UnmannedRobot class\n")

    unmanned_robot = RobotFactory.create_air_robot()
    unmanned_robot.start_mission()
    unmanned_robot.stop_mission()

    unmanned_robot = RobotFactory.create_ground_robot()
    unmanned_robot.start_mission()
    unmanned_robot.stop_mission()
    
    unmanned_robot = RobotFactory.create_surface_robot()
    unmanned_robot.start_mission()
    unmanned_robot.stop_mission()
    
    unmanned_robot = RobotFactory.create_undersea_robot()
    unmanned_robot.start_mission()
    unmanned_robot.stop_mission()
