import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        # self.publisher_ = self.create_publisher(String, 'topic', 10, qos_profile=qos.QoSPresetProfiles.SENSOR_DATA.value)
        self.publisher_ = self.create_publisher(String, 'topic', qos_profile=qos_profile_sensor_data)
        timer_period = 0.5  # seconds
        # self.times_dict = dict()
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher_.publish(msg)
    #     self.get_logger().info('Publishing: "%s"' % msg.data)
    #     time=self.get_clock().now().to_msg()
    #     int_time = int(str(time.sec) + str(time.nanosec))
    #     self.times_dict[int_time] = 1
    #     print(self.times_dict)
    #     self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
