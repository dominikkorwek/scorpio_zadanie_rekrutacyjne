#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import Float32


def UInt16_callback(msg: UInt16):
    a = msg.data
    cmd = Float32()
    
    if(a<2):                        #jezeli prekroczy zakres to trzeba wrocic do formatu prawidlowego
        a+=4095                     #

    cmd.data= 2*3.14* a / 4096      #obliczanie predkosci katowej
    
    pub.publish(cmd)                #wysylanie predkosci katowej


if __name__ == '__main__':
    rospy.init_node("velocity")
    pub = rospy.Publisher("/virtual_dc_motor_driver/get_velocity", Float32, queue_size= 10)
    sub = rospy.Subscriber("/virtual_dc_motor/get_position", UInt16, callback=UInt16_callback)
    rospy.loginfo("node dziala")
    rospy.spin()
  
