from abc import ABCMeta, abstractmethod

"""
Now, without ABCMeta
"""
class Robot():

    @abstractmethod
    def start_mission(self):
        pass

class SuperRobot(Robot):
    pass

sr = SuperRobot()
sr.start_mission()
print("First definition without ABCMeta passes\n")
# Mmmmmh, can be executed !

"""
Now, with ABCMeta
"""

class Robot(metaclass=ABCMeta):

    @abstractmethod
    def start_mission(self):
        pass

class SuperRobot(Robot):
    pass

try:
    sr = SuperRobot()
    sr.start_mission()
except Exception as e:
    print("Second definition with ABCMeta, ERROR !")
    print(e)