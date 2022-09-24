from ai2thor.controller import Controller
# from PIL import Image
import numpy as np
import cv2

class RobotKinematics:
    def __init__(self, controller: Controller, grid_size=0.1, angle_increment=10):
        self.controller = controller
        self.grid_size = grid_size
        self.angle_increment = angle_increment

    def display_depth(self):
        raw_depth_img = self.controller.last_event.depth_frame
        img = raw_depth_img/np.max(raw_depth_img)
        img *= 255
        cv2.imshow('Depth', img.astype(np.uint8))

    def display_instance_segmentation(self):
        raw_seg_img = self.controller.last_event.instance_segmentation_frame
        cv2.imshow('Instance segmentation', raw_seg_img.astype(np.uint8))

    def MoveAhead(self, distance):
        for _ in range(int(distance / self.grid_size)):
            self.controller.step(action="MoveAhead")
            # self.display_depth()

    def MoveBack(self, distance):
        for _ in range(int(distance / self.grid_size)):
            self.controller.step(action="MoveBack")
            # self.display_depth()


    def RotateLeft(self, rotate_amount):
        for _ in range(rotate_amount // 10):
            self.controller.step(action="RotateLeft", degrees=self.angle_increment)
            # self.display_depth()


    def RotateRight(self, rotate_amount):
        for _ in range(rotate_amount // 10):
            self.controller.step(action="RotateRight", degrees=self.angle_increment)
            # self.display_depth()


