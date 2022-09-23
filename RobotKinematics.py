from ai2thor.controller import Controller


class RobotKinematics:
    def __init__(self, controller: Controller, grid_size=0.1, angle_increment=10):
        self.controller = controller
        self.grid_size = grid_size
        self.angle_increment = angle_increment

    def MoveAhead(self, distance):
        for _ in range(int(distance / self.grid_size)):
            self.controller.step(action="MoveAhead")

    def MoveBack(self, distance):
        for _ in range(int(distance / self.grid_size)):
            self.controller.step(action="MoveBack")

    def RotateLeft(self, rotate_amount):
        for _ in range(rotate_amount // 10):
            self.controller.step(action="RotateLeft", degrees=self.angle_increment)

    def RotateRight(self, rotate_amount):
        for _ in range(rotate_amount // 10):
            self.controller.step(action="RotateRight", degrees=self.angle_increment)

