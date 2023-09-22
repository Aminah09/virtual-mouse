
# AI VIRTUAL MOUSE

## Description

The AI Virtual Mouse is a computer vision-based system that enables users to control the mouse cursor and perform mouse functions using hand gestures. It utilizes Python programming language and OpenCV library for hand gesture recognition and tracking

``` python version used - 3.8.5 ```

## Requirements

To run this project, you need the following:

- Python 3 (preferably Python 3.6 or later)
- Required Python libraries: OpenCV, NumPy, Autopy, Mediapipe

## Installation

Use the following commands to install the required Python libraries:

- OpenCV: `pip install opencv-python`(https://pypi.org/project/opencv-python/)
- NumPy: `pip install numpy`(https://pypi.org/project/numpy/)
- Autopy: `pip install autopy`(https://pypi.org/project/autopy/)
- Mediapipe: `pip install mediapipe`(https://pypi.org/project/mediapipe/)

## Usage

1. Clone this repository to your local machine or download the project files.

2. Install the required Python libraries if not already installed using the provided installation commands.

3. Launch a Python development environment.

4. Open the `vmdemo.py` script.

5. Run the script to start the AI Virtual Mouse.

6. Follow the on-screen instructions to perform various mouse actions using hand gestures.

7. Press 'Q' to quit the AI Virtual Mouse.


## Implementation and testing


![alt text](https://mediapipe.dev/images/mobile/hand_landmarks.png)


For the Mouse Cursor Moving around the Computer Window <br/>
``` if fingers[1] == 1 ``` i.e. the tip of index finger is up and and the remaining fingers are down it is in moving mode.

For the Mouse Cursor to perform button click <br/>
``` if fingers[1] == 1 and fingers[2] == 1: ``` i.e. both the tip of index finger and middle finger are up and the remaining are down.

## Project Structure

The project structure is as follows:

- `vmdemo.py`: The Python script that contains the implementation of the AI Virtual Mouse.

- `README.md`: This readme file providing an overview of the project and instructions for running it.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore and modify the code according to your needs. Enjoy using the AI Virtual Mouse!

 

