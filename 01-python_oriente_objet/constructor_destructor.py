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

        print("Hello I'm %s with %s%% battery"%(self.name, self.battery_level))
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
      print("%s Auto destruction NOW"%(self.name))
      global ROBOT_COUNT
      ROBOT_COUNT -= 1



if __name__ == '__main__':
    print(ROBOT_COUNT, ' robot(s) created')
    print('Creating robots...')

    r1 = Robot('Robotnik', battery_level=20)
    r2 = Robot(battery_level=100)

    print(ROBOT_COUNT, ' robot(s) created\n')


    print('Destroy %s now \n'%(r1.name))
    del r1

    print(ROBOT_COUNT, ' robot(s) created')
    print('\nEnd of program. Exit.\n')
