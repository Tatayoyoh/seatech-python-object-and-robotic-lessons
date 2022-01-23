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

if __name__ == '__main__':
    say_hello_to('Robert','Bob','Rayan')

    print()

    activate_driller()

    print()
