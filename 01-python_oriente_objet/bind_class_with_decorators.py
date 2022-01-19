class RobotAction(object):
    def __init__(self, f):
        self.__f = f

    def __call__(self, *args):
        print("it's a robot action")
        return self.__f(*args)

class RobotSafeAction(object):
    __is_dangerous = False

    def __init__(self, dangerous=False):
        print(dangerous)
        self.__is_dangerous = dangerous

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            if self.__is_dangerous:
                print('<WATCH OUT> ! Dangerous action incoming...')
                print('action was not triggered :)')
            else:
                print('<Keep calm> : Safe action incoming...')
                return f(*args, **kwargs)
        return wrapped



@RobotAction
@RobotSafeAction(dangerous=False)
def say_hello_to(guy1, guy2, guy3):
    print('Hello to:', guy1, guy2, guy3)

@RobotAction
@RobotSafeAction(dangerous=True)
def activate_driller():
    print('Driller activation: BbbBrrrrRrrr')

say_hello_to('Robert','Bob','Rayan')

print()

activate_driller()

print()

class RobotCore():
    _action_allowed = False
  
    @property
    def action_allowed(self):
        return self._action_allowed

    def allow_action(self):
        self._action_allowed = True

    def disable_action(self):
        self._action_allowed = False

    # it's a function, not a method
    def ActionAllowed(f):
        def wrapper(*args):
            self = args[0]
            if not self.action_allowed:
                print('Robot is not allowed to do any action... ', str(f))
            else:
                return f(*args)
        return wrapper


# creating class B
class Robot(RobotCore) :
    
    def __init__(self, action_allowed=False):
        self._action_allowed = action_allowed

    @RobotCore.ActionAllowed
    def fire(self):
        print('pew pew !')

    @RobotCore.ActionAllowed
    def run(self):
        print("let's goooo")



if __name__ == '__main__':
    r = Robot(action_allowed=True)
    r.fire()
    r.run()

    print()

    r = Robot(action_allowed=False)
    r.fire()
    r.allow_action()
    r.run()