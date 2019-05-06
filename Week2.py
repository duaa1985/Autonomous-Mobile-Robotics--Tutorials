#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor
 
This temporary script file is located here:
/home/user/.spyder2/.temp.py
"""
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
 
wheel_radius = 0.6
robot_radius = 0.8
 
def callback(data):
    (v, a) = forward_kinematics(data.data, 0)    
    t = Twist()
    t.linear.x = v
    t.angular.y = a
    publisher(t)
   
def publisher(t):
    pub = rospy.Publisher("/turtlebot_1/cmd_vel", Twist,queue_size = 10)  
    pub.publish(t)
   
def listener():
    rospy.Subscriber("/wheel_vel_left", Float32, callback)
    rospy.spin()
 
def forward_kinematics(w_l, w_r):
    c_l = wheel_radius * w_l
    c_r = wheel_radius * w_r
    v = (c_l + c_r) / 2
    a = (c_r - c_l) / (2 * robot_radius)
    return (v, a)
 
if __name__ == '__main__':
    rospy.init_node('fragments', anonymous=True)
    listener()
