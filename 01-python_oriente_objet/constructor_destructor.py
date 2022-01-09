ROBOT_COUNT = 0

class Robot():
    # Robot attributes
    name = "<unnamed>"
    
    # Constructor
    def __init__(self, name=None):
        if name:
            self.name = name
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
      print("%s Auto destruction NOW"%(self.name))
      global ROBOT_COUNT
      ROBOT_COUNT -= 1


r = Robot('Robotnik')

print("Hello %s"%(r.name))

del r