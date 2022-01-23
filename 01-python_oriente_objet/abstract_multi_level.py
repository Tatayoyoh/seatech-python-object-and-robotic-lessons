from abc import ABCMeta, abstractmethod, abstractproperty

class RobotVehicule(metaclass=ABCMeta):
    @abstractproperty
    def _running(self):
        pass

    @abstractmethod
    def status(self):
        pass

class UnmannedVehicule(RobotVehicule, metaclass=ABCMeta):
    @abstractmethod
    def start_mission(self):
        pass

class RemoteOperatedVehicule(RobotVehicule, metaclass=ABCMeta):
    @abstractmethod
    def execute(self, order):
        pass

class AutonomousVehicule(RobotVehicule, metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass


class FieldTypeVehicule():
    __field = None

    def __init__(self, field):
        self.__field = field

    @property
    def field(self):
        return self.__field


class AutonomousUnderseaVehicle(AutonomousVehicule, FieldTypeVehicule):
    # redefinition forced by RobotVehicule
    _running = False
    
    # redefinition forced by FieldTypeVehicule
    def __init__(self):
        FieldTypeVehicule.__init__(self, 'underwater')

    # redefinition forced by AutonomousVehicule
    def start(self):
        print('start autonomous mission')
        self._running = True

    # redefinition forced by RobotVehicule
    def status(self):
        print(self)

    def __str__(self):
        return 'AutonomousUnderseaVehicle [running:%s]'%(self._running)

auv = AutonomousUnderseaVehicle()
auv.start()
auv.status()
