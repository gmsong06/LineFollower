from wpilib.drive import DifferentialDrive


class Drivetrain(DifferentialDrive):
    def __init__(self, left_motor, right_motor):
        super().__init__(left_motor, right_motor)
        self.left_motor = left_motor
        self.right_motor = right_motor

    def move_forward(self, speed):
        self.arcadeDrive(0, -speed)

    def turn_left(self, rotation_speed):
        self.arcadeDrive(rotation_speed, 0)

    def turn_right(self, rotation_speed):
        self.arcadeDrive(-rotation_speed, 0)
