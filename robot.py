import wpilib
import os
from wpilib import TimedRobot, Joystick, Spark
from drivetrain import Drivetrain

class MyRobot(TimedRobot):
    def robotInit(self):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain(Spark(0), Spark(1))

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        turn = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, turn)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

if __name__ == "__main__":
    # ROMI ports
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)
