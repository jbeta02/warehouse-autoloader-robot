# Warehouse Autoloader Robot

Simulated warehouse robot capable of navigating warehouse autonomously using ROS2's slam-toolbox and nav2 stacks. A Franka Emika Panda robot arm is used to load and unload the robot with cargo. Simulated using Gazebo. 

## Tech Stack:

### Simulation and Testing:
- Custom and modified prebuilt urdf models of robots.
- Gazebo Classic for simulating robot usage in warehouse environment.
- RVIZ to test ROS2 states of robot.

### Transportation Robot
- Using slam_toolbox for localization and map creation.
- using Nav2 for robot navigation.
- Developed custom launch file for starting simulation, Rviz, spawn robot, and load warehouse world.
- Created custom urdf file for robot (using simplified robot, finalized version is work in progress).

### Loader Arm
- Using ROS2 Control for interacting with robot hardware.
- Custom launch file for starting simulation and spawn robot.
- Using MoveIt to control robot arm and trajectory execution.
- (Work in progress)

**Work in Progress. Full readme coming soon**

Recently accomplished: Successful SLAM and navigation tests on test transportation robot.

Currently working on: Integrating Panda arm with test transportation robot. 

Next: Add finilzed transportation robot model into Gazebo

<div align="center">
    <img src="assets/simulation_side.png" alt="design" width="75%">
</div>

<div align="center">
    <img src="assets/side_by_side.png" alt="design" width="75%">
</div>

<div align="center">
    <img src="assets/panda_arm.png" alt="design" width="75%">
</div>