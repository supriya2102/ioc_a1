🧠 Emotion Detection using Python + OpenCV + FER
📖 Overview

This project detects human emotions in real-time using your webcam.
It uses OpenCV for capturing video frames and the FER (Facial Emotion Recognition) library to identify emotions such as:

😄 Happy    😠 Angry    😢 Sad    😐 Neutral    😲 Surprise

The result is displayed live on the video feed with the emotion label and confidence score.
⚙️ Requirements

Make sure you have Python 3.8+ installed.

Install the required libraries using:

pip install opencv-python fer

💻 How to Run

Clone this repository:

git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector

Run the script:

python simple_emotion.py


Wait for the webcam window to open.
Press ‘q’ anytime to exit.

How It Works

The script captures frames from your webcam using OpenCV.

The FER library detects faces and predicts the dominant emotion.

The detected emotion and confidence score are:

Displayed on the frame

Printed in the terminal

Example output:

happy (0.95)
neutral (0.87)
sad (0.72)
