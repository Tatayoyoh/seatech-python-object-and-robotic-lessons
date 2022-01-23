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

    def is_flying(self):
        return self.__flying

    @property
    def flying(self):
        return self.__flying

    def speak(self):
        print('Hello from FlyingRobot')

class FlyingCyborg(Cyborg, FlyingRobot):
    pass



if __name__ == '__main__':
    print(heritage_description.__doc__)

    fly_cyb = FlyingCyborg('Deux Ex Machina', 'Female')

    # let's see if speak() is used from Cyborg or FluingRobot class !?
    pprint(FlyingCyborg.mro())
    print()
    print(fly_cyb.speak())
    print()

    # Robots and Human attributs
    print('I\'m',fly_cyb.name, fly_cyb.sexe, 'flying cyborg.')

    # Robot methods
    # fly_cyb.charge()
    fly_cyb.status()

    # Human methods
    fly_cyb.eat(['coca', 'chips'])
    fly_cyb.digest()

    # Cyborg methods
    fly_cyb.dance_funk()

    # FlyingRobot methods
    print('\n')
    
    fly_cyb.fly()
    if fly_cyb.is_flying():
        print('Regarder un oiseau !...')
        print('Non, c\'est un nuage !...')
        print('Non, c\'est un avion !...')
        print('Non, c\'est SUPERMAN !!!')
    fly_cyb.land()

    print()