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