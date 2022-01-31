from controller import Keyboard
from SeatechEpuckRobot import SeatechEpuckRobot

def get_keybord_pressed_keys():
    pressed_keys = []
    current_key = keyboard.getKey()
    while current_key != -1:
        pressed_keys.append(current_key)
        current_key = keyboard.getKey()
    return pressed_keys

if __name__ == '__main__':
    TIME_STEP = 64

    # create the Robot instance.
    robot = SeatechEpuckRobot()

    # Init keybopard control
    keyboard = Keyboard()
    keyboard.enable(samplingPeriod=200) # samplingPeriod in milliseconds

    print('Use UP/DOWN and LEFT/RIGHT keys to move E-Puck Robot')

    while robot.step(TIME_STEP) != -1:
        pressed_keys = get_keybord_pressed_keys()

        if not pressed_keys:
            robot.stop()
            continue

        # print('pressed_keys:', pressed_keys)
        if Keyboard.UP in pressed_keys and Keyboard.LEFT in pressed_keys:
            robot.run(left=True)
        elif Keyboard.UP in pressed_keys and Keyboard.RIGHT in pressed_keys:
            robot.run(right=True)
        elif Keyboard.UP in pressed_keys:
            robot.run()
        elif Keyboard.LEFT in pressed_keys:
            robot.turn_left()
        elif Keyboard.RIGHT in pressed_keys:
            robot.turn_right()
        elif Keyboard.DOWN in pressed_keys:
            robot.run(backward=True)
