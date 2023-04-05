from wpilib import DigitalInput
from drivetrain import Drivetrain


class LineFollower:
    def __init__(self, drivetrain: Drivetrain):
        self.left_sensor = DigitalInput(8)  # TODO: CHANGE THESE TO THE RIGHT PORTS
        self.right_sensor = DigitalInput(9)  # TODO: CHANGE THESE TO THE RIGHT PORTS
        self.drivetrain = drivetrain

    def run(self):
        left_sensor_value = self.left_sensor.get()
        right_sensor_value = self.right_sensor.get()

        while left_sensor_value or right_sensor_value:
            if left_sensor_value:
                print("Left sensor is on the line")
                self.drivetrain.turn_left(0.1)  # TODO: Potentially adjust rotation speed
            elif right_sensor_value:
                print("Right sensor is on the line")
                self.drivetrain.turn_right(0.1)  # TODO: Potentially adjust rotation speed

            left_sensor_value = self.left_sensor.get()
            right_sensor_value = self.right_sensor.get()

        self.drivetrain.move_forward(0.5)

    def test_left_sensor(self):
        return self.left_sensor.get()

    def test_right_sensor(self):
        return self.right_sensor.get()
