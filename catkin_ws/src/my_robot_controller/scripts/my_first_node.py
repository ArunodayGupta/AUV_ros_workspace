#!/usr/bin/env python3

import rospy

if __name__=='__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Hello from the test node")

    rate=rospy.Rate(0.2)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()