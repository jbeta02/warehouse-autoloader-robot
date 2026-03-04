setup:
install humble on ubuntu 22.04
install xacro
install joint state publisher gui

running:
ros2 launch warehouse_robot rsp.launch.py use_sim_time:=true
viz2 -d src/warehouse_robot/config/view_bot.rviz
ros2 run joint_state_publisher_gui joint_state_publisher_gui

ros2 launch warehouse_robot launch_sim.launch.py