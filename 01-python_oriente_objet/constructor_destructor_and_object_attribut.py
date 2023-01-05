
class Robot():
    name = "<unnamed>"
    power = False
    states = ['shutown', 'booting','running']
    
    def __init__(self, name=None):
        if name:
            self.name = name
        self.current_state = self.states[0]
        self.power = False

    def __del__(self):
        print("%s Auto destruction NOW"%(self.name))


if __name__ == '__main__':
    # Python permet d'appeler directement la propriétés d'une classe
    print("\nPython permet d'appeler directement la propriétés d'une classe")
    print("Robot.name: ", Robot.name)
    print("Robot.power: ", Robot.power)
    try:
        print(Robot.current_state)
    except AttributeError as e:
        print("Robot.current_state: ", e)

    # Oh la belle instance de classe : naissance d'un objet
    print("\nNaissance de l'objet Robot")
    r = Robot(name='Terminator')
    print("RobotObj.name: ", r.name)
    print("RobotObj.power: ", r.power)
    print("RobotObj.current_state: ", r.current_state)

    # Ceci n'a pas bougé
    print("\nAppel de current_state toujours indisponible à partir de la classe")
    print("Robot.name: ", Robot.name)
    print("Robot.power: ", Robot.power)
    try:
        print(Robot.current_state)
    except AttributeError as e:
        print("Robot.current_state: ", e)
