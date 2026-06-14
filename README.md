# AI-Powered Smart Waste Segregation System

## Overview

AI-Powered Smart Waste Segregation System is an intelligent waste management solution that automatically classifies and segregates waste into Dry, Wet, and Recyclable categories using Deep Learning, Computer Vision, and Arduino-based automation.

The system captures waste images through a camera, classifies them using a TensorFlow MobileNetV2 model, and automatically rotates the bin and opens the disposal flap using motors and servo control.

---

## Features

* Real-time waste classification using camera input
* Deep Learning based image recognition
* MobileNetV2 Transfer Learning
* Automated waste segregation
* Arduino-controlled motor rotation
* Servo-based flap mechanism
* LCD status display
* Dry, Wet, and Recyclable waste categorization
* Real-time communication between Python and Arduino

---

## Technologies Used

### Software

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* PySerial

### Hardware

* Arduino Uno
* Servo Motor
* DC Motor
* LCD I2C Display
* Camera Module

---

## Project Workflow

1. Capture waste image using camera.
2. Preprocess image and perform classification.
3. Predict waste category using MobileNetV2 model.
4. Send classification result to Arduino through serial communication.
5. Rotate bin to the correct compartment.
6. Open and close disposal flap automatically.
7. Display waste category and system status on LCD.

---

## Machine Learning Model

* Model: MobileNetV2
* Framework: TensorFlow / Keras
* Input Size: 224 × 224
* Classification Categories:

  * Dry Waste
  * Wet Waste
  * Recyclable Waste

---

## Repository Structure

* train.py
* waste_classifier_to_arduino.py
* realtime.py
* classifier.py
* converter.py
* Arduino Code
* Dataset
* Trained Model (.keras)

---

## Learning Outcomes

* Deep Learning and Transfer Learning
* Computer Vision with OpenCV
* Model Training and Validation
* Hardware-Software Integration
* Arduino Programming
* Serial Communication
* Smart Waste Management Systems

---

## Future Enhancements

* Mobile Application Integration
* Cloud-Based Monitoring Dashboard
* Additional Waste Categories
* IoT-Based Remote Monitoring
* Smart City Deployment

---

## Author

V S DeviKrishna

B.Tech Computer Science and Engineering

LBS Institute of Technology for Women
