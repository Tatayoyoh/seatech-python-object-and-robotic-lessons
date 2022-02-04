from SeatechEpuckRobot import SeatechEpuckRobot

if __name__ == '__main__':
    TIME_STEP = 64

    # create the Robot instance.
    robot = SeatechEpuckRobot(TIME_STEP)
    robot.track_object('rubber duck')

    while robot.step(TIME_STEP) != -1:
        running = robot.run()
        if robot.goal_reached:
            print('VICTORY !!')
            break

    robot.stop()

