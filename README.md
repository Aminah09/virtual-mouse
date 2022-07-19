
# AI VIRTUAL MOUSE

## Description

It is an AI virtual mouse system that makes use of the hand gestures and hand tip detection for performing mouse functions in the computer using computer vision.
Hand gesture and hand tip detection by using computer vision is used as a HCI with the computer. Python programming language is used for developing the AI virtual mouse system, and also OpenCV which is the library for computer vision is used in the AI virtual mouse system.

``` python version used - 3.8.5 ```

## Libraries

import math

import cv2 as cv

import numpy as np

import autopy

import mediapipe as mp

## Installation of python libraries

open-cv [pip install opencv-python](https://pypi.org/project/opencv-python/)

numpy [pip install numpy](https://pypi.org/project/numpy/)

autopy [pip install autopy](https://pypi.org/project/autopy/)

mediapipe [pip install mediapipe](https://pypi.org/project/mediapipe/)


## Implementation and testing

For the Mouse Cursor Moving around the Computer Window
``` if fingers[1] == 1 ``` i.e. the tip of index finger is up and and the remaining fingers are down it is in moving mode.

For the Mouse Cursor to perform button click
``` if fingers[1] == 1 and fingers[2] == 1: ``` i.e. both the tip of index finger and middle finger are up and the remaining are down.
 

