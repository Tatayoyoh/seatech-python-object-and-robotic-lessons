import time

ROBOT_COUNT = 0

class Robot():
    # Robot private attributes
    __name = '<unnamed>'
    __power = False
    __current_speed = 0
    __battery_level = 0
    __speaches = {'boot':'Hello world', 'shutdown':'Goodbye world'}
    __states = ['shutown', 'running']
    
    # Constructor
    def __init__(self, name=None):
        if name:
            self.__name = name
        self.__current_status = self.__states[0]
        self.__power = False
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
        print("%s Auto destruction NOW"%(self.__name))
        global ROBOT_COUNT
        ROBOT_COUNT -= 1

    """
    Encapsulation : Accessrors and Mutators
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def battery_level(self):
        return self.__battery_level

    @property
    def current_status(self):
        return self.__current_status

    def stop(self):   
        self.__current_speed = 0
      
    def move(self, speed):
        self.__current_speed = speed
      
    def speed(self):
        return self.__current_speed

    def boot(self):   
        self.__power = True
        self.__current_status = self.__states[1]
        print("%s, I'm %s [%s%% battery]"%(self.__speaches['boot'], self.name, self.battery_level))
      
    def shutdown(self):   
        self.__power = False
        self.__current_status = self.__states[0]
        self.__current_speed = 0
        print("%s, I'm %s"%(self.__speaches['shutdown'], self.name))
      
    def charge(self):   
        while self.__battery_level < 100:
            self.__battery_level += 20
            print("Charge is %s%%"%(self.battery_level))
            time.sleep(1)

    def status(self):
        print("%s status : %s [%s%% battery]"%(self.name, self.__current_status, self.battery_level))

    def is_running(self):
        return (self.__power == True)

    def speak(self):
        print('Hello from Robot')

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