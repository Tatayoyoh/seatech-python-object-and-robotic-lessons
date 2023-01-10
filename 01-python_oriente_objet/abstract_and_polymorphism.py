from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def start_mission(self, mission):
        pass

    @abstractmethod
    def stop_mission(self):
        pass

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass

    @abstractmethod
    def status(self):
        pass

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def move(self, forward=True):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def dive(self):
        pass

    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def status(self):
        pass

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def fly(self):
        print('Now in the sky')

    def land(self):
        print('Landed with success')

    def start_mission(self, mission):
        print('Aerial mission start :', mission)
        self.fly()

    def stop_mission(self):
        print('Aerial mission stop.')
        self.land()

    def status(self):
        print('Unmanned Aerial Vehicle')

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    def move(self, forward=True):
        print('Move [forward=%s]'%(forward))

    def stop(self):
        print('Move stopped')

    def start_mission(self, mission):
        print('Ground mission start :', mission)
        self.move()

    def stop_mission(self):
        print('Ground mission stop.')
        self.stop()

    def status(self):
        print('Unmanned Ground Vehicle')

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def dive(self):
        print('I dived')

    def surface(self):
        print('Sea surface reached')

    def start_mission(self, mission):
        print('Undersea mission start :', mission)
        self.dive()

    def stop_mission(self):
        print('Undersea mission stop.')
        self.surface()

    def status(self):
        print('Unmanned Undersea Vehicle')



uav = UAV()
uav.status()
uav.start_mission('scan the sky')
uav.stop_mission()
print()

ugv = UGV()
ugv.status()
ugv.start_mission('collect minerals')
ugv.stop_mission()
print()

uuv = UUV()
uuv.status()
uuv.start_mission('analyse whales')
uuv.stop_mission()
print()
