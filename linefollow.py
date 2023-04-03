import wpilib
from wpilib import DigitalInput, DigitalOutput

class LineFollower:
    def __init__(self):
        self.left_sensor = DigitalInput(0)  # TODO: CHANGE THESE TO THE RIGHT PORTS
        self.right_sensor = DigitalInput(1)  # TODO: CHANGE THESE TO THE RIGHT PORTS
        pass
    def run(self):
        left_sensor_value = self.left_sensor.get()
        right_sensor_value = self.right_sensor.get()

        if left_sensor_value:
            print("Left sensor is on the line")

        if right_sensor_value:
            print("Right sensor is on the line")

        # TODO: Add code to make the robot follow the line
