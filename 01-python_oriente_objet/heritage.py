from encapsulation_good_pratices import Robot

class LandTypeRobot(Robot):
    __land = None

    def __init__(self, name, land):
        self.__land = land
        super().__init__(name)

    def __del__(self):
        pass # do not print message enymore !

    @property
    def land(self):
        return self.__land

    def status(self):
        print("%s (%s) status: %s [%s%% battery]"%(self.name, self.land, self.current_status, self.battery_level))



class GroundRobot(LandTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'ground')

class AirRobot(LandTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'air')

class UnderseaRobot(LandTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'undersea')

class SurfaceRobot(LandTypeRobot):

    def __init__(self, name):
        super().__init__(name, 'surface')



if __name__ == '__main__':
    ugv = GroundRobot('Wall.E')
    uav = AirRobot('Megacopter')
    usv = UnderseaRobot('Nautilus')
    uuv = SurfaceRobot('Titaniktou')

    ugv.status()
    uav.status()
    usv.status()
    uuv.status()