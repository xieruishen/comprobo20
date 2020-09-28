#!/usr/bin/env python3
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped
import rospy # allows you to do something simple

rospy.init_node('point_publisher')
pub = rospy.Publisher('my_point', PointStamped, queue_size=10)

msg = PointStamped()
msg.header.frame_id = 'odom'
msg.point.x = 1
msg.point.y = 2

r = rospy.Rate(2)
while not rospy.is_shutdown():
    pub.publish(msg)
    print(msg)
    r.sleep()

rospy.spin()
