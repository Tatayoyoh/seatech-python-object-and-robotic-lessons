from abc import ABC
from abc import abstractmethod, abstractproperty
from abc import abstractclassmethod, abstractstaticmethod
import time

class TimeRobot(ABC):

    @abstractproperty
    def timezone(self):
        pass

    @abstractclassmethod
    def change_timezone(cls):
        pass

    @abstractstaticmethod
    def whattime():
        pass

    @abstractmethod
    def mission(self):
        pass

class Robot(TimeRobot):
    timezone = 'Europe/Paris'

    def change_timezone(cls, timezone):
        cls.timezone = timezone

    def whattime():
        print('We are', time.asctime())

    def mission(self):
        print('Timezone :', self.timezone)
        print('Start Robot missions...')


if __name__ == '__main__':
    try: # Can not use TimeRobot as object !
        rob = TimeRobot()
    except Exception as e:
        print(e,'\n')
    
    rob = Robot()
    Robot.whattime()
    rob.change_timezone('America/Montreal')
    rob.mission()
