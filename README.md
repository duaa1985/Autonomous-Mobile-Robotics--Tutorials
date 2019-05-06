![University of Lincoln](http://thelincolnite.co.uk/wp-content/uploads/2012/07/new_uni_crest.jpg "University of Lincoln")

----------
# Week 2: First steps with ROS Programming
  * [Preparation](#preparation)
     * [Your Real Robot (handling and programming)](#your-real-robot-handling-and-programming)
     * [On the simulated robot (gazebo)](#on-the-simulated-robot-gazebo)
  * [Mini Tasks of week 2:](#mini-tasks-of-week-2)
     * [Task 1: Make your robot move using the command line <em>(both, in simulation and real robot, see above)</em>:](#task-1-make-your-robot-move-using-the-command-line-both-in-simulation-and-real-robot-see-above)
     * [Task 2: Python programming](#task-2-python-programming)
  * [Summarised Assessment requirements for Minitask Week 2:](#summarised-assessment-requirements-for-minitask-week-2)
  * [Background that may help you](#background-that-may-help-you)


*Today, your team will also be starting with the real robot, in addition to the simulation. To work with the real robot, please follow the following steps. While you are waiting to get your robot, make sure to work in simulation as detailed below.*

## Preparation

*Remember, you are a group, so you may decide who is going to focus on real robot and who on simulation! Both attract marks for the mini task outlined below, solving them on the simulated robot first is often easier. So, you may designate a subteam to familiarise themselves with and work on the real robot and read the following in detail and then report back to the whole group, while the other group members already focus on the solution for the simulation.*

Recordings of the relevant parts of the lecture are on Blackboard in the Panopto folders, but also some recordings are on youtube from previous lectures (but will be slightly outdated!):
  1. Use of the commandline tools:  https://youtu.be/_2VmTefxCBk
  2. Python Programming: https://youtu.be/nHPDBJZWZqo


### Your Real Robot (handling and programming)

1. Get your turtlebot from the demonstrators!
1. Read [[Turtlebots]] and particularly familiarise yourself with the [handling of the robots](Turtlebots#handling-your-turtlebot) (anyone who is going to touch the real robot, please)!
1. In this workshop, we will be connecting to the turtlebots from our own desktop machines via the wireless network. Your turtlebots have an IP address assigned which you will be using to talk to them through ROS. So, find out the IP address of your robot after booting it up and try to [connect to it in your browser](Turtlebots#connecting-to-the-robot-from-your-browser).
1. Start the main drivers of the robot as described in [here](Turtlebots#starting-the-hardware-drivers-tmule-control).
1. You have two options to run code and commands on the robot, make sure you read about these [two options](Turtlebots#programming-the-robot). 

### On the simulated robot (gazebo)
* To work in simulation, start the simulator, see [last weeks tutorial](https://github.com/LCAS/teaching/blob/kinetic/uol_turtlebot_simulator/tutorial.md). 

## Mini Tasks of week 2:

### Task 1: Make your robot move using the command line *(both, in simulation and real robot, see above)*:
1. Run `rostopic list` and discuss with your team members what you see. Also try `rostopic echo /odom` and push the robot about if you're working on the real robot or make it move in simulation using the keyop from last week. What do you see?
1. use `rostopic pub` to make the robot move! Try to develop the following command using the `Tab` key for auto-completion (do not directly copy this, as it will not work): 

      ```
      rostopic pub /mobile_base/commands/velocity geometry_msgs/Twist "
      linear:
        x: 0.0
        y: 0.0
        z: 0.0
      angular:
        x: 0.0
        y: 0.0
        z: 0.5" -r 1 
      ```
    (You can stop this command by hitting `[Ctrl]-C` on your keyboard!)
    * In simulation, you already know how to do this
    * On the real robot, you may choose between running it on the robot in [Jupyter](Turtlebots#programming-in-jupyter) or via the [VPN setup](Turtlebots#connecting-via-vpn-from-pc). For this task, simply using the [terminal in Jupyter](Turtlebots#using-the-terminal-in-jupyter-to-issue-ros-commands) is by far the easiest.
1. Watch your turtlebot move (try simulation first). Explain (to your team and a demonstrator) what is happening. Try to make it go around in a circle (with about 0.5m radius) smoothly by modifying the above command.
1. *Optional, but very relevant:* run `roslaunch turtlebot_rviz_launchers view_robot.launch` again (you did last week?!) and in particular inspect the output of the real robot's sensors (for this to work you need to connect form your PC to the [real robot via VPN](Turtlebots#connecting-via-vpn-from-pc)!. Find out how to display different sensory information of the robots: Pointcloud, "laserscans" (discuss what this actually is, as there is no laser sensor on the robot!), and images. Show the demonstrator how your turtlebot sees the world.


### Task 2: Python programming

1. Read this tutorial on [how to create a publisher in python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29). Remember that we want to publish a `geometry_msgs/Twist` to `/mobile_base/commands/velocity`!
1. To create a workspace and package and start spyder correctly, please have a look at [[First Turtlebot coding]]
1. Time to code our first Python program using ROS: The goal is (again) to have the turtlebot first go around in a circle, this time from the Python program! 
  * In simulation, you just run the simulation as before, and then your code in Spyder or from the command line
  * On the real robot, you may choose between running it on the robot in [Jupyter](Turtlebots#programming-in-jupyter) or via the [VPN setup](Turtlebots#connecting-via-vpn-from-pc)
1. **Optional:** When you have accomplished this, the next challenge for you is to make it go in the shape of a square of 1m length each side.

## Summarised Assessment requirements for Minitask Week 2:

__The following needs to be accomplished to get full marks for this workshop. Remember, you can also still show the outcome of week 1 workshops and get full marks. Last chance in this second week!__

* For full marks your group needs to show your accomplishment in both tasks in simulation *and* on the robot
* You need to show that you can make your robot move (in simulation *and* reality), both, via the `rostopic` command line tool, and from your Python code.

## Background that may help you

**What to sent to the robot?***

A `Twist` message has two parts that are important:
* `Twist.linear`: this has x,y,z components for which you can specify the speed in m/s. Please don't go beyond 0.6
* `Twist.angular`: this also has x,y,z components and determines how quick the robot should rotate around one of the axes in radians/s. Please don't go beyond PI.
To determine which axis you want to move along and turn around, please have a look at the picture below:

    ![Turtlebot axes](turtlebot_axes.png)

_Red: x, green: y, blue: z_

# Week 3: Computer Vision with ROS and OpenCV

**Make sure you keep all your code you develop in the workshops and also note down any commands you used (create a `README.md` file for your notes). Maybe, a good idea is to actually keep all this in your own https://github.com repository (even share within your group). You will need this again as you go along in this module.**

In the lecture, you have been introduced to ways to conduct image processing in Python using [OpenCV](http://www.opencv.org/). In this workshop, you shall learn how to 

1. retrieve images from ROS topics (both simulator and optionally from the real robot, read [[Turtlebots]] again to recall how to do this)
1. convert images into the OpenCV format
1. perform image processing operations on the image
1. (optionally) command the robot based on your image processing output

To get you off the ground quickly, all the source code shown in the lecture is available [online](https://github.com/LCAS/teaching/tree/kinetic/cmp3103m-code-fragments/scripts). In particular, have a look at

* [`opencv_intro.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/opencv_intro.py) which shows you how to load an image in OpenCV without ROS and address it. Also look at the official [OpenCV Python tutorials](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html) to gain a better understanding
* [`opencv_bridge.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/opencv_bridge.py) showing you how to use [CvBridge](http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython) to read image from a topic. 
* [`color_contours.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/color_contours.py) to get an idea about colour slicing as introduced in the lecture. Also read about [Changing Colour Spaces](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces).

#### Tasks

*Make sure you call in a demonstrator to show your achievements to gain those marks* 

1. Develop Python code with the following abilities:
    1. Take the example code fragment [`opencv_bridge.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/opencv_bridge.py) from the lecture and modify it so you can read from the camera of your (simulated and real) turtlebots.
    1. read images from your (real and simulated) robot, display them using OpenCV methods, and try out colour slicing as presented in the lecture to segment a coloured object of your choice, both, in simulation or in reality. When trying this in simulation, put some nice coloured objects in front of the robot. Find suitable parameters to robustly segment that blob. You may take [`color_contours.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/color_contours.py) as a starting point for your implementation.
    1. Use the output from above to then publish `std_msgs/String` messages on a `Publisher` that contains information about the outcome of the operation (e.g. print the mean value of the pixel intensities of the resulting image). (Hint: You'll need to create a Publisher with type `std_msgs/String` for this: `p=rospy.Publisher('/result_topic', String)` and then publish to it.

    **Make sure to show your working code to demonstrators, having it working both in simulation and on the robot. Be prepared to discuss the differences you observe in simulation and reality. Running this on the robot this time requires you to use the [VPN setup](Turtlebots#connecting-via-vpn-from-pc). You cannot use Jupyter easily to display images in OpenCV**

1. (Optional) Research about Hough Transform and see how it can be used to detect lines with [OpenCV for Python](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html). Understand the concepts of Hough transform from your research and then also look at the circle detection code in [`hough_circle.py`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/scripts/hough_circle.py). Make it work with actual image data received via a topic from your (simulated/real) robot.
1. (Optional) Try out the "followbot" presented in the lecture. Take the code from https://github.com/marc-hanheide/ros_book_sample_code/tree/master/chapter12 described in chapter 12 of the "Programming Robots with ROS" book, available also on blackboard. *Note:* Make sure you allow the simulation to find the additional resources by first running ``export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:`pwd` `` (when in the directory of chapter 12) in the terminal you then run `roslaunch chapter12  course.launch` in afterwards. 

Also, browse through this collection of useful resources beyond what has been presented in the lecture in B3: [[OpenCV and ROS]]


# Week 4: Control and more Programming


Besides the following task, make sure you have caught up with all the previous tasks. 

**IMPORTANT:** You are expected to bring your source code from the previous workshop(s) to every workshop again. Also you are expected to take your own notes, e.g. about the commands you use, how things worked, etc, and have them available for every session. The workshops are successively building on top of each other. You need the knowledge from the previous workshops to engage in this one. It is strongly advised to store all your coding after every session. Best recommendation for this to use a source code repository, free to use from various providers, such as http://github.com or https://bitbucket.org/, for instance.

# Two Tasks for this week:

1. In the lecture the ["forward kinematics"](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/kinematics_diffdrive.py#L9-L14) and the ["inverse kinematics"](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/kinematics_diffdrive.py#L18-L23) for a robot with a differential drive (like the turtlebot) have been introduced. You already know that your turtlebot accepts a `geometry_msgs/Twist` message on the topic `/cmd_vel` to receive motion commands. This `Twist` message defines the linear velocity and the angular velocity, which the turtlebot driver converts into angular velocities ω using the "inverse kinematics". However, assume you want to command you robot using wheel angular velocity yourself, so, you want to define the angular velocities ω for each wheel. Then, you need to use the forward kinematics to find the values for a suitable `Twist` message from given ω values. Your task is to extend the [fragments from the lecture](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/kinematics_diffdrive.py) to 
    1. subscribe to a new topic `/wheel_vel_left` of type `std_msgs/Float32` (allows to send single float values)
    1. Take the input from the topic above and use it as the angular velocity (in rad/s) of the left wheel of your robot to then compute a `geometry_msgs/Twist` message to be published on `/cmd_vel`. Assume that the velocity of the right wheel is ω=0.0.
    1. adjust the [`robot_radius`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/kinematics_diffdrive.py#L5) and [`wheel_radius`](https://github.com/LCAS/teaching/blob/kinetic/cmp3103m-code-fragments/kinematics_diffdrive.py#L4) in our code to the correct values.
    1. Which behaviour of your robot do you expect when you run `rostopic pub /wheel_vel_left std_msgs/Float32 "data: 1.0" -r 10` while your implemented node is running? Does your robot behave as expected?
1. We shall now also move towards the assignment, so your first job here is to first launch a "training environment" (which you will use to develop in for your individual coursework): `roslaunch uol_turtlebot_simulator object-search-training.launch`. Then:
    * Write a little bit of Python code (extending on your last week's work of finding objects via colour slicing) to drive towards *one* of the coloured cylinders. You may, in addition to your own solution from last week, take the line [follower robot implementation](https://github.com/marc-hanheide/ros_book_sample_code/blob/master/chapter12/src/follower_p.py) of a proportional line-following controller as a guide here.
    * All you need to do is to control the robot's angular velocity according to the position of the detected box. So, your robot's task is to chase after one specific colour. 
    * You are allowed to bump into it, but you may already think about how to stop about 1m away from the box and *not* bump into it.
    * You only have to get this to work in simulation, but you *may* also implement colour chasing behaviour on the real robot!

**Make sure to show your work to a demonstrator! To be ticked off this week, you need to show**

1. **Python code working to send velocities on the `/wheel_left_vel` and have the robot only moving its left wheel using the forward kinematics model, and**
2. **your implementation of a simple colour chasing behaviour as outlined above**

## Remarks
* This is the last of the mini tasks, so make sure you complete this in your group and you really fully understand what the code you produced as a group does. From now on, you will be working towards your individual assignment. Make sure you read the assessment brief again and ask anything unclear as soon as possible.
* You can still show your achievements for week B3 this week to get full marks (including on the real robot!). Likewise, you can show this week's work also next week to still get full marks. You have missed the opportunity to get full marks for the tasks of weeks B1 and B2 now, but you can still get 50% if you show it now.
* Make sure to work as a group, possibly having different members initially working on different sub-tasks and then bringing them back together!
