#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

x=0
y=0

def update_position(data):
    global x,y
    x=data.x
    y=data.y

def print_position():
    print(f"The x-coordinate : {x:.2f} , The y-coordinate : {y:.2f}")

def turtle_controller():
    rospy.init_node('bot')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    print("Commands: 1. up\n, 2. down\n, 3. left\n, 4. right\n")
    
    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown():
        command = input("Enter command : ").strip().lower()
        distance= int(input("Enter the distance you want to move : "))
        
        move_command = Twist()
        
        if command == "up":
            move_command.linear.y = distance 
            rospy.Subscriber('/turtle1/pose', Pose, update_position)
            print_position()
        elif command == "down":
            move_command.linear.y = -distance
            rospy.Subscriber('/turtle1/pose', Pose, update_position)
            print_position()
        elif command == "right":
            move_command.linear.x = distance 
            rospy.Subscriber('/turtle1/pose', Pose, update_position)
            print_position()
        elif command == "left":
            move_command.linear.x = -distance
            rospy.Subscriber('/turtle1/pose', Pose, update_position)
            print_position()
        else:
            print("Invalid command")
            continue
        
        end_time = rospy.Time.now() + rospy.Duration(1.0)
        while rospy.Time.now() < end_time:
            pub.publish(move_command)
            rate.sleep()

if __name__ == '__main__':
    try:
        turtle_controller()
    except rospy.ROSInterruptException:
        pass