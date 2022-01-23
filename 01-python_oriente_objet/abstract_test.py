from abc import ABC, abstractmethod

"""
Now, without ABC
"""
class Robot():

    @abstractmethod
    def start_mission(self):
        pass

class SuperRobot(Robot):
    pass

sr = SuperRobot()
sr.start_mission()
print("First definition without ABC passes\n")
# Mmmmmh, can be executed !

"""
Now, with ABC
"""

class Robot(ABC):

    @abstractmethod
    def start_mission(self):
        pass

class SuperRobot(Robot):
    pass

try:
    sr = SuperRobot()
    sr.start_mission()
except Exception as e:
    print("Second definition with ABC, ERROR !")
    print(e)