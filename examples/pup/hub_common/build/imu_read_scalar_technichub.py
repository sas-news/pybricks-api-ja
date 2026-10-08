from pybricks.hubs import TechnicHub
from pybricks.parameters import Axis
from pybricks.tools import wait

# Initialize the hub.
hub = TechnicHub()

# Get the acceleration or angular_velocity along a single axis.
# If you need only one value, this is more memory efficient.
while True:
    # Read the forward acceleration.
    forward_acceleration = hub.imu.acceleration(Axis.X)

    # Read the yaw rate.
    yaw_rate = hub.imu.angular_velocity(Axis.Z)

    # Print the yaw rate.
    print(yaw_rate)
    wait(100)
