#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8MultiArray

class BumpDectorNode(object):
    def __init__(self):
        rospy.init_node('bump_detector_node')
        self.linear_velocity = Twist()
        self.linear_velocity.linear.x = 2
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/bump', Int8MultiArray, self.process_bump)

    def process_bump(self, msg):
        for i in range(4):
            if msg.data[i] == 1:
                self.linear_velocity.linear.x = 0
                break

    def run(self):
        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            self.pub.publish(self.linear_velocity)
            r.sleep()

if __name__=='__main__':
    node = BumpDectorNode()
    node.run()
