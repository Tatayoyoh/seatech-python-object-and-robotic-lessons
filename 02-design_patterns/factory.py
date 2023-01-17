from abc import ABCMeta, abstractmethod, abstractproperty 

class UnmannedRobot(metaclass=ABCMeta):
    @abstractmethod
    def start_mission(self):
        pass

    @abstractmethod
    def stop_mission(self):
        pass

class FieldTypeRobot():
    __field = None
    mission = None

    def __init__(self, field):
        self.__field = field

    @property
    def field(self):
        return self.__field

class GroundRobot(UnmannedRobot, FieldTypeRobot):
    """ A ground vehicle """

    def __init__(self):
        FieldTypeRobot.__init__(self, 'ground')

    def start_mission(self):
        print("%s: Let's explore fields !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class AirRobot(UnmannedRobot, FieldTypeRobot):
    """ An aerial vehicle """

    def __init__(self):
        FieldTypeRobot.__init__(self, 'air')

    def start_mission(self):
        print("%s: Let's liftoff in the air !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class UnderseaRobot(UnmannedRobot, FieldTypeRobot):
    """ An undersea vehicle """

    def __init__(self):
        FieldTypeRobot.__init__(self, 'undersea')

    def start_mission(self):
        print("%s: Let's dive captain !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class SurfaceRobot(UnmannedRobot, FieldTypeRobot):
    """ A sea surface vehicle """

    def __init__(self):
        FieldTypeRobot.__init__(self, 'surface')

    def start_mission(self):
        print("%s: Let's ride on the sea !"%(self.field.capitalize()))

    def stop_mission(self):
        print("%s mission stopped."%(self.field.capitalize()))

class RobotFactory():
    @staticmethod
    def create_air_robot() -> UnmannedRobot:
        return AirRobot()

    @staticmethod
    def create_ground_robot() -> UnmannedRobot:
        return GroundRobot()

    @staticmethod
    def create_surface_robot() -> UnmannedRobot:
        return SurfaceRobot()

    @staticmethod
    def create_undersea_robot() -> UnmannedRobot:
        return UnderseaRobot()

if __name__ == '__main__':

    print("We will play with 'start_mission' and 'stop_mission' from child objects of UnmannedRobot class\n")

    unmanned = RobotFactory.create_air_robot()
    unmanned.start_mission()
    unmanned.stop_mission()
    print()

    unmanned = RobotFactory.create_ground_robot()
    unmanned.start_mission()
    unmanned.stop_mission()
    print()
    
    unmanned = RobotFactory.create_surface_robot()
    unmanned.start_mission()
    unmanned.stop_mission()
    print()

    unmanned = RobotFactory.create_undersea_robot()
    unmanned.start_mission()
    unmanned.stop_mission()
