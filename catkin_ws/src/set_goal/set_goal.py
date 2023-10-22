#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32


if __name__ == '__main__':
    rospy.init_node("set_goal")
    pub = rospy.Publisher("/virtual_dc_motor_controller/set_velocity_goal", Float32, queue_size= 10)
    rospy.loginfo("node dziala")
    rate= rospy.Rate(15)

    while not rospy.is_shutdown():
        msg = Float32()
        msg.data= 1                    #tutaj trzeba ustawic wymog predkosci
        
        pub.publish(msg)                #nie wiedzialem jak mozna subskrybowac w czasie rzeczywistym zmane parametrow, dlatego zeby 
        rate.sleep()                    #zmienic wymog trzeba na nowo wlaczyc node

  
