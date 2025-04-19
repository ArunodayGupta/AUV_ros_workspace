#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    result = msg.data + 5
    rospy.loginfo(f"receieved value : {msg.data}, Final value: {msg.data} + 5 = {result}")

def sub2():
    rospy.init_node('Adding_5')
    rospy.Subscriber('chatter_2', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    sub2()