#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import Float32

def receive_deg_cb(msg):
     count = msg.data* math.pi/180
     rospy.loginfo(f"{msg.data}, {count}")

if __name__ == '__main__':
     rospy.init_node('deg2rad')
     sub = rospy.Subscriber("/deg_topic",Float32, receive_deg_cb)
     rospy.spin()
