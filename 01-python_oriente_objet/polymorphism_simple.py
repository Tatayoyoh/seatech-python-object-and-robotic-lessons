from encapsulation_good_pratices import Robot

class FieldTypeRobot():
    __field = None
    __name = None

    def __init__(self, name, field):
        self.__field = field
        self.__name = name

    def __del__(self):
        pass # do not print message anymore !

    def start_mission(self):
        print(f"%s starting \033[1m\033[93m%s\033[0m mission"%(self.__name, self.__field))

class GroundRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'ground')

    def ride(self):
        print('Moving on ground...')

class AirRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'air')

    def fly(self):
        print('Flying strait...')

class UnderseaRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'undersea')

    def dive(self):
        print('Diving undersea...')

class SurfaceRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'surface')

    def ride(self):
        print('Moving on sea...')    



def use_robots_for_mission(robot: FieldTypeRobot) -> bool:
    """
        On attend ici un type FieldTypeRobot, ou tout autre classe hérité de FieldTypeRobot
    """
    robot.start_mission()

    try:
        robot.ride()
    except Exception as e:
        print(e, "  << mauvais appel, on est allé trop loin dans l'attente de l'objet")
    finally:
        print()


if __name__ == '__main__':

    robots = [
        GroundRobot('Wall.E'),
        AirRobot('Megacopter'),
        UnderseaRobot('Nautilus'),
        SurfaceRobot('Titaniktou'),
    ]

    for rob in robots:
        use_robots_for_mission(rob)