#!/usr/bin/env python
# BEGIN ALL
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
 
class Follower:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("window", 1)
    cv2.namedWindow("Segmentation", 2)
    self.image_sub = rospy.Subscriber('/turtlebot_1/camera/rgb/image_raw',
                                      Image, self.image_callback)
    self.cmd_vel_pub = rospy.Publisher('/turtlebot_1/cmd_vel_mux/input/teleop',
                                       Twist, queue_size=1)
    self.twist = Twist()
  def image_callback(self, msg):
    try:
       cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
       print e
    image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = numpy.array([ 60,  165,  100])
    upper_yellow = numpy.array([125, 255, 255])
    lower_green = numpy.array([60, 165, 100])
    upper_green = numpy.array([125,255,255])
    hsv_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    hsv_thresh = cv2.inRange(hsv_img,lower_green,upper_green)
    mask = cv2.inRange(hsv, lower_green, upper_green)
   
    h, w, d = image.shape
    search_top = 3*h/4
    search_bot = 3*h/4 + 20
    mask[0:search_top, 0:w] = 0
    mask[search_bot:h, 0:w] = 0
    M = cv2.moments(mask)
    print(M)
    if M['m00'] > 0:
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv2.circle(image, (cx, cy), 20, (0,0,255), -1)
      # BEGIN CONTROL
      err = cx - w/2
      self.twist.linear.x = 0.2
      self.twist.angular.z = -float(err) / 100
      self.cmd_vel_pub.publish(self.twist)
      # END CONTROL
 
    cv2.imshow("window", image)
    cv2.waitKey(3)
 
    cv2.imshow("Segmentation", hsv_thresh)
 
rospy.init_node('follower')
follower = Follower()
rospy.spin()
# END ALL