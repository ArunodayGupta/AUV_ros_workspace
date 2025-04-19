#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    result = msg.data * 10
    pub.publish(result)
    rospy.loginfo(f"Received value : {msg.data}, Multiplied value : {result}")

def sub1():
    global pub
    rospy.init_node('multiplying_by_10')
    pub = rospy.Publisher('chatter_2', Int32, queue_size=10)
    rospy.Subscriber('chatter_1', Int32, callback)
    rospy.spin()

if __name__=='__main__':
    sub1()