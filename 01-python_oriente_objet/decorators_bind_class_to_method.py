class RobotCore():
    # it's a function, not a method
    def SecurisedAction(f):
        def wrapper(*args):
            obj = args[0]
            if obj.safety_enabled:
                print('Robot is not allowed to do any action... ', str(f))
            else:
                return f(*args)
        return wrapper


class Robot() :
    
    def __init__(self, safety=False):
        self.__safety = safety

    @property
    def safety_enabled(self):
        return self.__safety

    def enable_safety(self):
        self.__safety = True

    def disable_safety(self):
        self.__safety = False

    @RobotCore.SecurisedAction
    def fire(self):
        print('pew pew !')

    @RobotCore.SecurisedAction
    def run(self):
        print("let's goooo")


if __name__ == '__main__':
    r = Robot(safety=True)
    r.fire()
    r.run()

    print()

    r = Robot(safety=False)
    r.fire()
    r.enable_safety()
    r.run()