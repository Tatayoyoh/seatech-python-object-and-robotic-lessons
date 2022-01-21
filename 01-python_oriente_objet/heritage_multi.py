from encapsulation_good_pratices import Robot
import time
import sys

class Human():   
    __sexe = None
    __stomac_content = []

    def __init__(self, sexe):
        self.__sexe = sexe

    @property   
    def sexe(self):
        return self.__sexe

    def eat(self, food):   
        if type(food) is str:
            food = [food]
        self.__stomac_content += food
        print('Miam, delicious ', ' and '.join(food))

    def digest(self):   
        while len(self.__stomac_content):
            print('Digest ', self.__stomac_content.pop(), '...')
            time.sleep(1)

        print('*Glouglouglouglou noises are coming from belly...*')

    def speak(self):
        print('Hello from Human')

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def dance_funk(self):
        print("Let's dance !!")
        print("https://youtu.be/cZzK32Cfcq8")
        for x in range(0, 3):
            sys.stdout.write('╘[◉﹃◉]╕\r')
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write('┏[◉﹃◉]┛\r')
            sys.stdout.flush()
            time.sleep(1)

    def speak(self):
        print('Hello from Cyborg')

if __name__ == '__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.dance_funk()