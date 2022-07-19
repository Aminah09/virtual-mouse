
# AI VIRTUAL MOUSE

## Description

It is an AI virtual mouse system that makes use of the hand gestures and hand tip detection for performing mouse functions in the computer using computer vision.
Hand gesture and hand tip detection by using computer vision is used as a HCI with the computer. Python programming language is used for developing the AI virtual mouse system, and also OpenCV which is the library for computer vision is used in the AI virtual mouse system.

## Libraries

import cv2 as cv

import numpy as np

import autopy

import mediapipe as mp

import math

>Installation of python libraries 
>[opencv](pip install opencv-python)
>[numpy](pip install numpy)
>[autopy](pip install autopy)
>[mediapipe](pip install mediapipe)
>, numpy, autopy , mediapipe)
>
>my python version was 3.8 


# Test Video
if you use your Index Finger you can adjust and move the mouse

if you want to click all you have to do is raising your middle finger and putting it next to your Index

# Explian code 
 we have writen hand Tracking module before and you have to read it before since we used this module in this prj 
 
 first we have to import some libraries that we need in this code
 
 then we have import our VideoCamera using cv2 libraries 
 
 then we have detect the hand if there is a hand or not 
 
 in the next step we need to get the position of INDEX and MIDDLE FINGER as x,y to use them to control our mouse 
 
 following this step we have to detect which finger is up ( INDEX or MIDDLE and INDEX) 
 
 if Index is up so we have to write a program as moving mode
  > so we need to detect the position of our finger and make an area that we have to move our finger in 
  > 
  > then we need to turn our finger position to our Screen size 
 
 and if Index and Middle finger is up we have to CLICK 
