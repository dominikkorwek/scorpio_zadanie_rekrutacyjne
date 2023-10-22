#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32
import message_filters


def callback(goal: Float32, velocity: Float32):
    cmd= Int8()
    cmd.data = 0     
    g=goal.data
    v=velocity.data
    
    if(g<v-1):              #
        cmd.data+=-50       #
    if(g < v):              #jak predkosc jest wieksza niz wymog predkosci to wysyla dane o zmniejszeniu obrotow
        cmd.data += -13     #

    if(g>v+1):              #
        cmd.data+=50        #
    if(g > v):              #jak predkosc jest mniejsza niz wymog predkosci to wysyla dane o zmniejszeniu obrotow
        cmd.data += 13      #

    if(g==v):               #
        cmd.data = 10       #jak predkosc byla by rowna wymogowi to wysyla dane o utrzymaniu predkosc ( zauwazylem ze dla 10 mniej wiecej utrzymuje)
    pub.publish(cmd)


if __name__ == '__main__':
    rospy.init_node("controller")
    pub = rospy.Publisher("/virtual_dc_motor/set_cs", Int8, queue_size= 10)
    sub1 = message_filters.Subscriber("/virtual_dc_motor_controller/set_velocity_goal", Float32)
    sub2 = message_filters.Subscriber("virtual_dc_motor_driver/get_velocity", Float32)
    ts=message_filters.ApproximateTimeSynchronizer([sub1,sub2],queue_size=10,slop=0.1,allow_headerless=True)
    ts.registerCallback(callback)
    rospy.loginfo("node dziala")    


    rospy.spin()


