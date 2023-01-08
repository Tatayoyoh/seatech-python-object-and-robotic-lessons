from encapsulation_good_pratices import Robot

class FieldTypeRobot(Robot):
    __field = None

    def __init__(self, name, field):
        self.__field = field
        super().__init__(name)

    def __del__(self):
        pass # do not print message anymore !

    @property
    def field(self):
        return self.__field

    def status(self):
        print("%s (%s) status: %s [%s%% battery]"%(self.name, self.field, self.current_status, self.battery_level))

    def start_mission(self):
        if self.is_running():
            print(f"Starting \033[1m\033[93m%s\033[0m mission !\n"%(self.field))
        else:
            print('Boot robot first !')

class GroundRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'ground')

class AirRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'air')

class UnderseaRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'undersea')

class SurfaceRobot(FieldTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'surface')



if __name__ == '__main__':
    ugv = GroundRobot('Wall.E')
    uav = AirRobot('Megacopter')
    usv = UnderseaRobot('Nautilus')
    uuv = SurfaceRobot('Titaniktou')

    ugv.status()
    ugv.start_mission()
    ugv.boot()
    ugv.start_mission()
    
    uav.status()
    uav.boot()
    uav.start_mission()

    usv.status()
    usv.boot()
    usv.start_mission()

    uuv.status()
    uuv.boot()
    uuv.start_mission()