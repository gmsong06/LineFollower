import commands2
import wpilib
import wpilib.drive

class Drivetrain(commands2.SubsystemBase):
    def __init__(self, left_motor, right_motor):
        super().__init__()
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def arcadeDrive(self, forward, turn):
        self.drivetrain.arcadeDrive(forward, turn)

    def tankDrive(self, left, right):
        self.drivetrain.tankDrive(left, right)
