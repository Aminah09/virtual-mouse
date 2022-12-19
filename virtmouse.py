import math 
##import pycode_similar   													  # math class is used to derive the formula to find the distance between two coordinates
import pyautogui,mediapipe as mp,cv2 as cv,numpy as np            # short notations
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume      # Python Core Audio Windows Library
from ctypes import cast, POINTER                                  # returns a new instance of type which points to the same memory block as obj. type must be a pointer type
from comtypes import CLSCTX_ALL                                   # define, call, and implement custom and dispatch-based COM interfaces

prev_locx,prev_locy=0,0
curr_locx,curr_locy=0,0
factor=8
frames=100

w_S, h_S = 640, 480                # window in which the capture will bw seen
cap = cv.VideoCapture(0)
cap.set(3,w_S)
cap.set(4,h_S)
cap.set(5,120)


class HandsDetect():
    def __init__(self, status=False, maxHands=2, modelComplexity=1, detection_confidence=0.5, tracking_confidence=0.5):   # it is the sensitivity of hand feature detection, values can vary depending on lighting , camera quality
        self.status = status
        self.maxHands = maxHands                                       # tracking- Minimum confidence value (between 0 and 1) for the hand detection to be considered successful. Defaults- 0.5.
        self.modelComplex = modelComplexity                            # detection- Minimum confidence value (between 0 and 1) for the hand landmarks to be considered tracked successfully. Default- 0.5.
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        self.mpHands = mp.solutions.hands    					# class that will help us recognize all 20 geometric points on the hand. 
        self.hands = self.mpHands.Hands(self.status, self.maxHands, self.modelComplex,
                                        self.detection_confidence, self.tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
    
    
    def PosTrack(self, frame, handNo=0, draw=True, color =  (255, 0, 255), z_axis=False):
        landmarks_list = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):            #changing hand points coordinates into image pixels
                h, w, c = frame.shape           # height, width color of image                               
                if z_axis == False:
                   cx, cy = int(lm.x * w), int(lm.y * h)       # x,y coordinates of each point
                   landmarks_list.append([id, cx, cy])
                elif z_axis:
                    cx, cy, cz = int(lm.x * w), int(lm.y * h), round(lm.z,3)
                    landmarks_list.append([id, cx, cy, cz])     # x,y,z coordinates of each point
                if draw:
                    cv.circle(frame, (cx, cy),5,color, cv.FILLED)         # color, radius thickness of circle
        return landmarks_list                                          # circle each handpoint that have been identified.
    
    
    
    
    def track_hands(self, frame, draw=True):
        framesgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)           # change the format of image before we process it because opencv work on BGR format (Blue Green Red) 
        self.results = self.hands.process(framesgb)                # but mediapipe works on RGB (Red Green Blue)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:                     # check if there is any multi_hand_landmarks available basically we are checking for frames with hands in it
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, hand_landmarks,    # draw the points on hand landmark and connect them
                                               self.mpHands.HAND_CONNECTIONS)   # connect the points with line
        return frame
    
def main():
    cap = cv.VideoCapture(0)
    detector = HandsDetect(maxHands=1)                               # draw one hand at a time
    while True:
        ret, frame = cap.read()
        frame=cv.flip(frame,1)
        frame = detector.track_hands(frame)
        landmarks_list = detector.PosTrack(frame,z_axis=True,draw=False)
        if len(landmarks_list) != 0:
            print(landmarks_list[4])
        cv.imshow("img", frame)
        if cv.waitKey(1) ==27:
            break

        if (fingers == [0,0,0,0,0]) & (stat == 0 ):
            status='None'
        elif (fingers == [0, 1, 1, 1, 0] ) & (stat == 0 ):                   # Three fingers displaying on camera 
            status = 'Scroll'
            stat = 1
        elif (fingers == [1 ,1 , 1, 1, 1] ) & (stat == 0 ):                   # five fingers diaplaying on camera
             status = 'Cursor'
             stat = 1

             if len(landmarks_list) != 0:
                 if fingers[-1] == 1:
                     stat = 0
                     status = 'None'
                     print(status)
                 else:
                    x1, y1 = landmarks_list[4][1], landmarks_list[4][2]         #thumb cmc carbometacarpal , Metacarpophalangeal (MCP)
                    x2, y2 = landmarks_list[8][1], landmarks_list[8][2]         
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    cv.circle(frame, (x1, y1), 10, (0,215,255), cv.FILLED)         # yellow color to show contact line between finger points
                    cv.circle(frame, (x2, y2), 10, (0,215,255), cv.FILLED)
                    cv.line(frame, (x1, y1), (x2, y2), (0,215,255), 3)
                    cv.circle(frame, (cx, cy), 8, (0,215,255), cv.FILLED)
                    length = math.hypot(x2 - x1, y2 - y1)
                    
                    
                    
                    vol = np.interp(length, [height_min, height_max], [min_vol, max_vol])
                    volBar = np.interp(vol, [min_vol, max_vol], [400, 150])                     # volume bar dimension
                    volpercentage = np.interp(vol, [min_vol, max_vol], [0, 100])                # volume percentage dimension
                    print(vol)
                    volfinal = int(vol)
                    
                
                    vol.SetMasterVolumeLevel(volfinal, None)
                    if length < 40:                                                               # displaying the output
                        cv.circle(frame, (cx, cy), 11, (0, 0, 255), cv.FILLED)        # red color when volume is zero (circle)
                    cv.rectangle(frame, (30, 150), (55, 400), (0, 255, 0), 3)        # green color for volume bar
                    cv.rectangle(frame, (30, int(volBar)), (55, 400), (0, 255, 0), cv.FILLED)    #green color when volume max or min
                    cv.putText(frame, f"{int(volpercentage)}%", (25, 430), cv.FONT_HERSHEY_COMPLEX, 0.9, (220, 210, 0), 3)
    																								# vol percentage color
    
    
    
    if status == 'Cursor':
        stat = 1
        
        putText(status)
        cv.rectangle(frame, (frames, frames), (w_S-frames, h_S-frames), (255, 255, 255), 3)     # rectangle color white
        if fingers[1:] == [0,0,0,0]: 
            stat = 0
            status ='None'
            print(status)
        else:
            if len(landmarks_list) != 0:
                x1, y1 = landmarks_list[8][1], landmarks_list[8][2]
                x2,y2=landmarks_list[12][1:]
                w, h = pyautogui.size()
                x3 = int(np.interp(x1, [frames, w_S-frames], [0, w]))
                y3 = int(np.interp(y1, [frames,h_S-frames], [0, h ]))
                cv.circle(frame, (landmarks_list[8][1], landmarks_list[8][2]), 7, (255, 255, 255), cv.FILLED)    # white circle used as cursor
                
                x4,y4=int((x1+x2)/2),int((y1+y2)/2)
                x5,y5=landmarks_list[12][1],landmarks_list[12][2]
                lengthx=math.hypot(x5-x2,y5-y2)
                if fingers[1]==1 and fingers[0]==1:
                    curr_locx=prev_locx+(x3-prev_locx)/factor
                    curr_locy=prev_locy+(y3-prev_locy)/factor
                    pyautogui.moveTo(2*curr_locx,2*curr_locy)
                    prev_locx,prev_locy=curr_locx,curr_locy
                                  # on click
                if fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1:         # right click operation
                    pyautogui.click(button='right',interval=1)


    if status=='Scroll':
        stat=1
        putText(status)
        
        if len(landmarks_list)!=0:
            if fingers==[0,1,1,1,0]:
                # up   scroll
                putText(status = 'Up', loc=(190, 40), color = (0, 0, 255))         # BGR color red
                pyautogui.scroll(100)
            if fingers == [0,1,1,1,1]:
                # down   scroll
                putText(status = 'Down', loc =  (190, 40), color = (0, 0, 255))
                pyautogui.scroll(-100)
            elif fingers == [0, 0, 0, 0, 0]:
                stat = 0
                status = 'None'
    cv.imshow('Air Window',frame)

    def putText(status,loc = (10, 40), color = (255,0, 255)):       #text color magenta
        cv.putText(frame, str(status), loc, cv.FONT_HERSHEY_DUPLEX,2, color, 2)