#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from pymoveit2 import MoveIt2



class PandaMove(Node):

    def __init__(self):
        super().__init__("panda_move_node")

        self.arm = MoveIt2(
            node=self,
            joint_names=[
                "panda_joint1",
                "panda_joint2",
                "panda_joint3",
                "panda_joint4",
                "panda_joint5",
                "panda_joint6",
                "panda_joint7",
            ],
            base_link_name="panda_link0",
            end_effector_name="panda_hand",
            group_name="panda_arm",
        )


        self.gripper = MoveIt2(
            node=self,
            joint_names=[
                "panda_finger_joint1",
                "panda_finger_joint2",
            ],
            base_link_name="panda_hand",
            end_effector_name="panda_hand",
            group_name="hand",
        )

        self.get_logger().info("MoveIt2 interface initialized")


    def move_to_target(self):

        # target end-effector pose
        # panda arm range:
        # x: ~0.2 – 0.7 m
        # y: ~-0.4 – 0.4 m
        # z: ~0.1 – 0.7 m
        position = [0.5, 0.4, 0.5]
        quat_xyzw = [0.0, 1.0, 0.0, 0.0] # define rotation in quaternions (smooth interpolation, stable rotations, no gimbal lock)

        self.get_logger().info("Moving to target pose...")

        self.arm.move_to_pose(
            position=position,
            quat_xyzw=quat_xyzw,
            cartesian=False
        )

        self.arm.wait_until_executed()

        self.close_gripper()

        self.get_logger().info("Motion complete")


    def open_gripper(self):
        self.gripper.move_to_configuration([0.04, 0.04])
        self.gripper.wait_until_executed()


    def close_gripper(self):
        self.gripper.move_to_configuration([0.0, 0.0])
        self.gripper.wait_until_executed()

def main():

    rclpy.init()

    node = PandaMove()

    node.move_to_target()

    rclpy.shutdown()


if __name__ == "__main__":
    main()