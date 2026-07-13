#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MissionCommander(Node):

    def __init__(self):
        super().__init__('mission_commander')

        self.publisher_ = self.create_publisher(
            String,
            '/mission_status',
            10
        )

        self.missions = [
            "Searching",
            "Driving",
            "Collecting Sample",
            "Returning Home"
        ]

        self.index = 0

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

        self.get_logger().info("Mission Commander Started")


    def publish_status(self):

        msg = String()

        msg.data = self.missions[self.index]

        self.publisher_.publish(msg)

        self.get_logger().info(f"Publishing: {msg.data}")

        self.index = (self.index + 1) % len(self.missions)


def main(args=None):

    rclpy.init(args=args)

    node = MissionCommander()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
