ROS2 Talker & Listener (Python)
📖 Overview

This mini-project demonstrates basic Publisher–Subscriber communication in ROS2 using Python’s rclpy library.
It includes two nodes:

🗣️ talker.py → Publishes messages

👂 listener.py → Subscribes and listens to messages

🧩 Nodes Description
🗣️ talker.py

Publishes text messages of type std_msgs.msg.String to a topic named "topic" at regular intervals.

👂 listener.py

Subscribes to the same topic ("topic") and prints the messages it receives from the talker.
Concepts Used

ROS2 Node creation

Publisher and Subscriber setup

Topic-based communication

Callback functions in Python

Message passing using std_msgs.msg.String

⚙️ Requirements

ROS2 (Humble / Iron / Jazzy or compatible version)

Python 3.x

Properly sourced ROS2 environment
