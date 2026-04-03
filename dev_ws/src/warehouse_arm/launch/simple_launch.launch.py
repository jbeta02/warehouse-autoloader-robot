import os

from ament_index_python.packages import get_package_share_directory

from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from moveit_configs_utils import MoveItConfigsBuilder

from launch_ros.actions import Node


def generate_launch_description():

    package_name='warehouse_arm'
    pkg_path = get_package_share_directory(package_name)

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    pkg_path,'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # moveit_config = (
    #     MoveItConfigsBuilder("moveit_resources_panda")
    #     .robot_description(
    #         file_path="desciption/panda_copy.urdf",
    #         mappings={
    #             "ros2_control_hardware_type": LaunchConfiguration(
    #                 "ros2_control_hardware_type"
    #             )
    #         },
    #     )
    #     .robot_description_semantic(file_path="config/panda.srdf") # config/panda.srdf
    #     .trajectory_execution(file_path="config/gripper_moveit_controllers.yaml")
    #     .planning_pipelines(
    #         pipelines=["ompl", "chomp", "pilz_industrial_motion_planner"]
    #     )
    #     .to_moveit_configs()
    # )

    # # Start the actual move_group node/action server
    # move_group_node = Node(
    #     package="moveit_ros_move_group",
    #     executable="move_group",
    #     output="screen",
    #     parameters=[moveit_config.to_dict()],
    #     arguments=["--ros-args", "--log-level", "info"],
    # )


    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py",
            )
        )
    )

    # world = os.path.join(get_package_share_directory('warehouse_robot'),'worlds','warehouse_world_full.world') # warehouse_world_with_B   warehouse_world
    # # Include the Gazebo launch file, provided by the gazebo_ros package
    # gazebo = IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource([os.path.join(
    #                 get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    #                 launch_arguments={
    #                     'world': world
    #                     }.items()
    # )


    spawn_panda = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "panda"
        ],
        output="screen",
    )

    # urdf_file = os.path.join(pkg_path, "description", "panda_copy.urdf")

    # with open(urdf_file, "r") as infp:
    #     robot_description_content = infp.read()

    # robot_description = {"robot_description": robot_description_content}

    # controller_yaml = os.path.join(
    #     pkg_path,
    #     "config",
    #     "panda_controllers.yaml"
    # )

    # ros2_control_node = Node(
    #     package="controller_manager",
    #     executable="ros2_control_node",
    #     parameters=[robot_description, controller_yaml], # robot_description, controller_yaml
    #     output="screen",
    # )

    joint_state_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["panda_arm_controller"],
    )


    return LaunchDescription([
        rsp,

        # moveit_config,
        # move_group_node,

        gazebo,
        spawn_panda,

        # rviz_node

        # ros2_control_node,
        joint_state_spawner,
        arm_controller_spawner,

    ])