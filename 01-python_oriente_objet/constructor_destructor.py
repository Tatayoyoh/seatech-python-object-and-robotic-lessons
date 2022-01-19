ROBOT_COUNT = 0

class Robot():
    # Robot attributes
    name = "<unnamed>"
    battery_level = 0
    
    # Constructor
    def __init__(self, name=None, battery_level=0):
        if name:
            self.name = name
        self.battery_level = battery_level
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
      print("%s Auto destruction NOW"%(self.name))
      global ROBOT_COUNT
      ROBOT_COUNT -= 1

if __name__ == '__main__':
    print(ROBOT_COUNT, ' robot(s) created')
    r1 = Robot('Robotnik')
    r2 = Robot()

    print(ROBOT_COUNT, ' robot(s) created')

    print("Hello %s"%(r1.name))
    print("Hello %s"%(r2.name))

    print('Destroy %s now'%(r1.name))
    del r1

    print(ROBOT_COUNT, ' robot(s) created')

    print('End of program. Exit.')
