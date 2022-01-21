from encapsulation_good_pratices import Robot

class FieldTypeRobot(Robot):
    __field = None

    def __init__(self, name, field):
        self.__field = field
        super().__init__(name)

    def __del__(self):
        pass # do not print message enymore !

    @property
    def field(self):
        return self.__field

    def status(self):
        print("%s (%s) status: %s [%s%% battery]"%(self.name, self.field, self.current_status, self.battery_level))

    def start_mission(self):
        print(f"Starting \033[1m\033[93m%s\033[0m mission !"%(self.field))

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
    print()
    
    uav.status()
    uav.start_mission()
    print()

    usv.status()
    usv.start_mission()
    print()

    uuv.status()
    uuv.start_mission()