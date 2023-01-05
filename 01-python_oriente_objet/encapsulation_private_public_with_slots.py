class Robot():
    # private attributes with slots
    __slots__ = ('__current_speed', '__name', '__type')

    def __init__(self):
      self.__current_speed = 0
      self.__name = '<unnamed>'
      self.__type = 'human destructor'

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


if __name__ == '__main__':
  r = Robot()
  print('Accès aux attributs déclarés')
  r.name = "Terminator"
  r.move(100)
  print(r.name, r.type)
  print()

  print("Modification via le Mutateur 'move':")
  r.move(100)
  print("Récupération via l'Accesseur 'speed':", r.speed())
  print()

  try:
    print("Tentative de création d'un attribut à la volée nommé 'hacked'")
    r.hacked = 'ET BIM ! '
  except AttributeError as e:
    print(e)
