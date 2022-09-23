from ai2thor.controller import Controller
from PIL import Image

controller = Controller(
    agentMode="default",
    visibilityDistance=1.5,
    scene="FloorPlan212",

    # Step sizes
    grid_size=0.25,
    snapToGrid=True,
    rotateStepDegrees=90,

    renderDepthImage=False,
    renderInstanceSegmentation=False,

    # Camera perspectives
    width=600,
    height=600,
    fieldOfView=110

)

key = ""

while key != "q":
    key = input("Enter key: w/a/s/d & k/l: ")

    if key == "w":
        controller.step("MoveAhead")
    elif key == "a":
        controller.step("MoveLeft")
    elif key == "d":
        controller.step("MoveRight")
    elif key == "s":
        controller.step("MoveBack")
    elif key == "k":
        controller.step("RotateLeft")
    elif key == "l":
        controller.step("RotateRight")
    # elif key == "u":
    #     img = event.depth_frame
    #     img.show(title='Depth')
    controller.step("LookDown", angle=0)

controller.step(action="Done")
