from SeatechEpuckRobot import SeatechEpuckRobot

if __name__ == '__main__':
    TIME_STEP = 64

    # create the Robot instance.
    robot = SeatechEpuckRobot()

    while robot.step(TIME_STEP) != -1:
        robot.run()