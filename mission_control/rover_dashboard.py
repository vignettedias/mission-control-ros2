#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RoverDashboard(Node):

    def __init__(self):
        super().__init__('rover_dashboard')

        self.subscription = self.create_subscription(
            String,
            '/mission_status',
            self.status_callback,
            10
        )

        self.get_logger().info("Rover Dashboard Started")

    def status_callback(self, msg):
        self.get_logger().info(f"[Dashboard] Current Mission: {msg.data}")


def main(args=None):

    rclpy.init(args=args)

    node = RoverDashboard()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
