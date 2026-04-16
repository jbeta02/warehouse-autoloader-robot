#!/bin/bash

cd dev_ws
sudo rm -rf build install log # delete old builds so colcon build works (doesn't see old build paths)
colcon build
source install/setup.bash

ros2 launch warehouse_robot launch_sim.launch.py