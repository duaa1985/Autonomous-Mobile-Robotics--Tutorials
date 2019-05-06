#!/usr/bin/env python
 
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32 ,String
from sensor_msgs.msg import LaserScan
 
 
class Follower:
    global forward_kinematics
    wheel_radius =numpy.float32(0.6)
    robot_radius =numpy.float32(0.8)
    w_r = 0.0
    w_l = 0.0
    def __init__(self):
 
        cv2.namedWindow("window", 1)
 	cv2.namedWindow("mask", 2)
        cv2.startWindowThread()
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/turtlebot_2/camera/rgb/image_raw",
                                          Image, self.callback)
	self.cmd_vel_pub = rospy.Publisher('/turtlebot_2/cmd_vel_mux/input/teleop',
                                       Twist, queue_size=1)
	self.wheel_pub = rospy.Publisher('/wheel_vel_left',Float32,queue_size = 10)
	self.twist = Twist()
	self.stop = False

    def forward_kinematics(w_l, w_r):
     	c_l = Follower.wheel_radius * w_l
     	c_r = Follower.wheel_radius * w_r
     	v = (c_l + c_r) / 2
     	a = (c_r - c_l) / (2 * Follower.robot_radius)
     	return (v, a)
 
    def callback(self, msg):
	image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	self.wheel_pub.publish(0.1) 
	    
	(v,a) = forward_kinematics(Follower.w_l,Follower.w_r)

	lower_green = numpy.array([60,165,100])
	upper_green = numpy.array([125,255,255])
	mask = cv2.inRange(hsv, lower_green, upper_green)

	h, w, d = image.shape
	search_top = 1*h/4
	search_bot = 3*h/4 + 20
	mask[0:search_top, 0:w] = 0
	mask[search_bot:h, 0:w] = 0
	M = cv2.moments(mask)
	#cv2.imshow("Image window", cv_image)
        #cv2.imshow("Segmentation", hsv_thresh)
	#print("pies", M['m00'])
	print("pies", M)

	if M['m00'] > 0:
      		cx = int(M['m10']/M['m00'])
      		cy = int(M['m01']/M['m00'])
     		cv2.circle(image, (cx, cy), 20, (0,0,255), -1)
      		# BEGIN CONTROL
		if self.stop == False:
	      		err = cx - w/2
	      		self.twist.linear.x = 0.1
	      		self.twist.angular.z = -float(err) / 100
	      		self.cmd_vel_pub.publish(self.twist)
      		# END CONTROL
    	cv2.imshow("window", image)
	cv2.imshow("mask", mask)
    	cv2.waitKey(3)
 
Follower()
rospy.init_node('image_converter', anonymous=True)
rospy.Rate(10)
rospy.spin()
cv2.destroyAllWindows()
