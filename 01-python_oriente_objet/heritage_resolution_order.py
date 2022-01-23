from pprint import pprint

class Human():
    pass

class Robot():
    pass

class FlyingRobot(Robot):
    pass

# try change here
class Cyborg(Human, Robot):
    pass

# try change here
class FlyingCyborg(Cyborg,FlyingRobot):
    pass

def heritage_description():
    """
    Diamond heritage description :

    Human          Robot
         \        /      \ 
           Cyborg         FlyingRobot
                  \      /
                FlyingCyborg    
    """
    pass

print(heritage_description.__doc__)
pprint(FlyingCyborg.mro())