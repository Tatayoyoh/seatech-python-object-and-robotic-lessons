from math import copysign

class EpuckMotors():
    def __init__(self, robot_ref):
        self.left_motor = robot_ref.getDevice('left wheel motor')
        self.left_motor.setPosition(float('inf'))
        self.right_motor = robot_ref.getDevice('right wheel motor')
        self.right_motor.setPosition(float('inf'))

    def run(self, speed=None, left=False, right=False):
        """Run forward or backward but never over Epuck max speed"""
        max_speed = self.get_max_speed()
        if speed is None: # half speed by default
            speed = max_speed / 2
        if abs(speed) > abs(max_speed): # not more than max speed
            speed = copysign(max_speed, speed)
        
        left_speed = speed
        right_speed = speed
        # print(speed, left, right)
        if left:
            left_speed = 0
        elif right:
            right_speed = 0
        
        # run motors
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)

    def turn_left(self):
        self.left_motor.setVelocity(-self.get_max_speed())
        self.right_motor.setVelocity(self.get_max_speed())

    def turn_right(self):
        self.left_motor.setVelocity(self.get_max_speed())
        self.right_motor.setVelocity(-self.get_max_speed())


    def get_max_speed(self):
        """Max speed of the two wheels, divided by 2"""
        return (self.left_motor.getMaxVelocity() + self.right_motor.getMaxVelocity())/2