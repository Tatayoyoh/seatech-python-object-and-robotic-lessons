import time
import zoneinfo
from abc import ABCMeta
from abc import abstractmethod

class TimeRobot(metaclass=ABCMeta):

    """
        !!! ATTENTION !!!
        L'ordre est hyper important :
        
        @abstractmethod doit être annoté après les autres décorateurs
    """

    @property
    @abstractmethod
    def timezone(self):
        pass

    @classmethod
    @abstractmethod
    def default_timezone(cls):
        pass

    @staticmethod
    @abstractmethod
    def whattime():
        pass

    @timezone.setter
    @abstractmethod
    def timezone(self):
        pass

    @abstractmethod
    def mission(self):
        pass

class Robot(TimeRobot):
    __timezone = 'Europe/London'

    @property
    def timezone(self):
        return self.__timezone 

    @classmethod
    def default_timezone(cls):
        return cls.__timezone

    @staticmethod
    def whattime():
        print('We are', time.asctime())

    @timezone.setter
    def timezone(self, timezone):
        if timezone in zoneinfo.available_timezones():
            self.__timezone = timezone
        else:
            raise Exception('Oops, unavailable time !')

    def mission(self):
        print('Start Robot mission : travel in time...')
        print('Original    Timezone :', self.default_timezone())
        print('Destination Timezone :', self.timezone)


if __name__ == '__main__':
    
    try: # Can not use TimeRobot as object !
        rob = TimeRobot()
    except TypeError as e:
        print(e)
    
    rob = Robot()

    print()
    Robot.whattime()
    print()

    rob.timezone = 'America/Montreal'
    rob.mission()

