#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('multiple_of_2')
    pub=rospy.Publisher("chatter_1",Int32,queue_size=10)
    rate=rospy.Rate(1)
    num=0

    while not rospy.is_shutdown():
        pub.publish(num)
        rospy.loginfo("The published number is : %d", num)
        num += 2
        rate.sleep()

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass