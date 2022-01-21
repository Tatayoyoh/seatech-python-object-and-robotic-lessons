from pprint import pprint

class Human():
    pass

class Robot():
    pass

class FlyingRobot(Robot):
    pass

# try change here
class Cyborg(Robot, Human):
    pass

# try change here
class FlyingCyborg(FlyingRobot, Cyborg):
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