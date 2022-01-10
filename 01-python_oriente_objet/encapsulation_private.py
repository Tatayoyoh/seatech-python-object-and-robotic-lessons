class Robot():
    # private attributes
    __name = '<unnamed>'
    __current_speed = 0
    
    # simple style
    def stop(self):
      self.__current_speed = 0
    
    def move(self, speed):
      if type(speed) == int:
        self.__current_speed = speed
      
    def speed(self):
      return self.__current_speed
    
    # getter / setter style
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        self.__name = new_name

r = Robot()
r.name = "Termonator"
r.move(100)
print(r.name + "\nSpeed:", r.speed())
