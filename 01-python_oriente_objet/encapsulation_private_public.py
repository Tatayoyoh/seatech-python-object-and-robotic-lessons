class Robot():
    # private attributes
    __current_speed = 0
    __name = '<unnamed>'
    __type = 'human destructor'
    # protected attributes
    _nickname = 'Rob'
    
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
  print(r.name)
  r.name = "Terminator"
  r.move(100)
  print(r.name)
  print(r.type)
  print("Speed:", r.speed())
  print()

  try: 
    print("> Tentative d'accès direct à l'attribut privé '__name'")
    print(r.__name)
  except AttributeError as e:
    print(e)
  print("> Python3 protège par défaut l'accès aux attributs préfixés par __")
  print()

  print("> Tentative d'accès direct à l'attribut protected '_nickname'")
  print(r._nickname)
  r._nickname = 'Hacked Rob'
  print("> Modification de '_nickname'")
  print(r._nickname)
  print()

  print("> Tentative de création d'un nouvel attribut nommé 'hacked'")  
  r.hacked = 'Et BIM !'
  print(r.hacked)
  print("Il est possible de créer des attributs à la volée")
