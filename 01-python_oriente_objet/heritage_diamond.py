from pprint import pprint
from encapsulation_good_pratices import Robot
from heritage_multi import Cyborg
from heritage_resolution_order import heritage_description

class FlyingRobot(Robot):
    __flying = False

    def fly(self):
        print('Flying to the sky')
        self.__flying = True

    def land(self):
        print('Back to the earth')
        self.__flying = True

    @property
    def flying(self):
        return self.__flying

    def speak(self):
        print('Hello from FlyingRobot')

class FlyingCyborg(Cyborg, FlyingRobot):
    pass



if __name__ == '__main__':
    print(heritage_description.__doc__)

    fly_cyb = FlyingCyborg('Deux Ex Machina', 'M')

    # From Cyborg or FluingRobot class ??
    pprint(FlyingCyborg.mro())
    print()
    print(fly_cyb.speak())
    print()

    print(fly_cyb.name, 'sexe', fly_cyb.sexe)
    print('Charging battery...')

    # Robot methods
    fly_cyb.charge()
    fly_cyb.status()

    # Human methods
    fly_cyb.eat(['coca', 'chips'])
    fly_cyb.digest()

    # Cyborg methods
    fly_cyb.dance_funk()

    # FlyingRobot methods
    fly_cyb.fly()
    fly_cyb.land()