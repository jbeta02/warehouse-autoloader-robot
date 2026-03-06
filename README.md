setup:
install humble on ubuntu 22.04
install xacro
install joint state publisher gui
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control

source install/setup.bash
colcon build --symlink-install

running:
ros2 launch warehouse_robot rsp.launch.py use_sim_time:=true
viz2 -d src/warehouse_robot/config/view_bot.rviz
ros2 run joint_state_publisher_gui joint_state_publisher_gui

ros2 launch warehouse_robot launch_sim.launch.py


testing:
to teleop robot: ros2 run teleop_twist_keyboard teleop_twist_keyboard
to test ros2_control setup: ros2 control list_hardware_interfaces
use if publishing to diff_cont/cmd_vel_unstamped: ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
open rviz: rviz2 -d src/warehouse_robot/config/laser_scan.rviz