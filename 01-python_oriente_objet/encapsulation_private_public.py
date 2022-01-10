class Robot():
    # private attributes
    __current_speed = 0
    __name = '<unnamed>'
    __type = 'human destructor'
    # public attributes
    name2 = "j'aime pas coder pour rien :("
    
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

    @property
    def type(self):
        return self.__type
        
r = Robot()
print(r.name)
r.name = "Termonator"
r.move(100)
print(r.name)
print(r.type)
print("Speed:", r.speed())

print()
print(r.name2)
r.name2 = 'Et vous ?'
print(r.name2)
print()
print("On voit que déclarer '__name' en privé revient au même que déclarer 'name2' en publique niveau interface d'utilisation")
