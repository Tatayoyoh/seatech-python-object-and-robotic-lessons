import time

ROBOT_COUNT = 0

class Robot():
    # Robot attributes
    name = "<unnamed>"
    power = False
    current_speed = 0
    battery_level = 0
    speaches = {'boot':'Hello world', 'shutdown':'Goodbye world'}
    states = ['shutown', 'running']
    
    # Constructor
    def __init__(self, name=None):
        if name:
            self.name = name
        self.current_status = self.states[0]
        self.power = False
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
        print("%s Auto destruction NOW"%(self.name))
        global ROBOT_COUNT
        ROBOT_COUNT -= 1

    """
    Encapsulation : Accessrors and Mutators
    """

    def stop(self):   
        self.current_speed = 0
      
    def move(self, speed):
        self.current_speed = speed
      
    def speed(self):
        return self.current_speed

    def boot(self):   
        self.power = True
        self.current_status = self.states[1]
        print("%s, I'm %s [%s%% battery]"%(self.speaches['boot'], self.name, self.battery_level))
      
    def shutdown(self):   
        self.power = False
        self.current_status = self.states[0]
        self.current_speed = 0
        print("%s, I'm %s"%(self.speaches['shutdown'], self.name))
      
    def charge(self):   
        while self.battery_level < 100:
            self.battery_level += 10
            print("Charge is %s%%"%(self.battery_level))
            time.sleep(1)

    def status(self):
        print("%s status : %s [%s%% battery]"%(self.name, self.current_status, self.battery_level))

    def is_running(self):
        return (self.power == True)



if __name__ == '__main__':
    r = Robot(name="Robotnik")
    r.status()
    r.boot()
    r.status()
    r.charge()
    r.shutdown()
    r.status()

    print("\nEncore encore !")
    r.status()
    r.boot()
    r.status()
    r.charge()
    r.shutdown()
    r.status()