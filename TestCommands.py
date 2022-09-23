import time

from ai2thor.controller import Controller

controller = Controller(
    agentMode="locobot",
    visibilityDistance=1.5,
    scene="FloorPlan_Train1_3",

    # Step sizes
    grid_size=0.1,
    snapToGrid=True,
    renderDepthImage=False,
    renderInstanceSegmentation=False,
    width=600,
    height=600,
    fieldOfView=110
)

# Teleport to a certain position and orientation
controller.step(
    action="Teleport",
    position=dict(x=0.999, y=1.01, z=-0.3541),
    rotation=dict(x=0, y=90, z=0),
    horizon=30
)

# move the camera to an angle of -30 degrees
controller.step(action="LookUp")

# move the camera down to an angle of 30 degrees
controller.step(action="LookDown")

# move the robot forward the grid amount
controller.step(action="MoveAhead")

# move the robot back the grid amount
controller.step(action="MoveBack")

# rotate the robot left 90 degrees
controller.step(action="RotateLeft")

# rotate the robot right 90 degrees
controller.step(action="RotateRight")

# Exit unity
controller.step(action="Done")
