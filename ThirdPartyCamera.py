from RobotKinematics import RobotKinematics
import cv2
# import tensorflow as tf
import numpy as np

from ai2thor.controller import Controller
from ai2thor.platform import CloudRendering
controller = Controller(platform=CloudRendering)

renderDepthImage = True
renderInstanceSegmentation = True
renderSemanticSegmentation = False
renderNormalsImage = False

controller.reset(
    width=800,
    height=800,

    grid_size=0.1,

    renderDepthImage=renderDepthImage,
    renderInstanceSegmentation=renderInstanceSegmentation,
    renderSemanticSegmentation=renderSemanticSegmentation,
    renderNormalsImage=renderNormalsImage,
    # fieldOfView=140,
)

# Randomize the lighting in the room
controller.step(
    action="RandomizeLighting",
    brightness=(0.5, 1.5),
    randomizeColor=True,
    saturation=(0.5, 1),
    synchronized=True
)

# Change the materials to random states
controller.step(
    action="RandomizeMaterials"
)

# Custom controller object to make movement simpler
robot = RobotKinematics(controller)

# model = tf.keras.applications.resnet50.ResNet50(weights="imagenet")

if __name__ == '__main__':
    robot.RotateRight(240)
    controller.step("LookDown")

    robot.display_instance_segmentation()
    robot.display_depth()

    robot.add_third_party_camera()

    cv2.waitKey(0)
    controller.step(action="Done")

