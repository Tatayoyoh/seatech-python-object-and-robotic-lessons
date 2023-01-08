import sys, time
from abc import ABCMeta, abstractmethod

class Member(metaclass=ABCMeta):
    @abstractmethod
    def move(self): # moving action
        pass

class Leg(Member):
    def move(self):
        print('Do leg moving logic')

class Arm(Member):
    def move(self):
        print('Do leg moving logic')
  
class Head(Member):
    def move(self):
        print('Do head moving logic')
  
class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def fire(self):
        pass
      
class Laser(Weapon):
    def fire(self):
        print('Zap zap zap !')
        
class Rocket(Weapon):
    def fire(self):
        print('BOOOOM !')


class Human():
    def __init__(self):
        self.head = Head()
        self.left_leg = Leg()
        self.right_leg = Leg()
        self.left_arm = Arm()
        self.right_arm = Arm()

    def walk(self, meters=0):
        # for m in range(meters):
        #     self.right_leg.move()
        #     self.left_leg.move()
        print('  O ')
        print(' / \ ')
        for x in range(3):
            sys.stdout.write(' J \\\r')
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write(' / L\r')
            sys.stdout.flush()
            time.sleep(1)
        print()

class Robot():
    def charge(self):
        print('Charging battery')

class Cyborg(Human, Robot):
    def __init__(self):
        Human.__init__(self)
        Robot.__init__(self)
        self.laser = Laser()
        self.rocket = Rocket()

cyb = Cyborg()
cyb.charge()
cyb.walk(meters=20)
cyb.laser.fire()
cyb.rocket.fire()