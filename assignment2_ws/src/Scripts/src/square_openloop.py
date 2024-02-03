#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move():
	rospy.init_node('robot_cleaner', anonymous=True)
	rate = rospy.Rate(10)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	# Calculating distance of each side
	i = 0
	while(i<4):
		current_dist = 0
		while(current_dist < 2):
			t0 = rospy.Time.now().to_sec()
			vel_msg.linear.x = 0.2
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 0
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			# Distance
			current_dist = current_dist + 0.2*(t1-t0)
			
		vel_msg.linear.x = 0
		velocity_publisher.publish(vel_msg)
		
		current_orient = 0
		t0 = rospy.Time.now().to_sec()
		#Changing orientation
		while(current_orient < (math.pi)/2):
			vel_msg.angular.z = 0.2
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			current_orient = 0.2*(t1-t0)
			
		vel_msg.angular.z = 0
		velocity_publisher.publish(vel_msg)		
		i = i+1

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass

