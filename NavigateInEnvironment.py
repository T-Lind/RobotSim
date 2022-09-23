from ai2thor.controller import Controller
from RobotKinematics import RobotKinematics
import cv2

controller = Controller()#platform=CloudRendering)

renderDepthImage = True
renderInstanceSegmentation = False
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
    fieldOfView=140,
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

if __name__ == '__main__':
    robot.RotateLeft(90)

    for _ in range(2):
        robot.MoveAhead(1)
        robot.RotateRight(180)

    robot.MoveAhead(0.1)
    robot.RotateLeft(90)
    robot.MoveAhead(0.1)

    # controller.step(
    #     action="PickupObject",
    #     objectId="Mug|1|1|1"
    # )

    robot.MoveBack(0.1)


    robot.RotateRight(90)
    robot.MoveAhead(0.9)
    robot.RotateLeft(30)

    robot.display_depth()
    cv2.waitKey(0)


    controller.step(action="Done")
