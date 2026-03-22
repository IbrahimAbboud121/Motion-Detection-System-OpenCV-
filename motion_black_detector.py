import cv2 as cv 
import numpy as np

video = cv.VideoCapture(0)

def GetFrame():
    istrue, frame = video.read()
    frame = cv.flip(frame, 1)
    return frame

current_frame = GetFrame()

while True:
    next_frame = GetFrame() 
    blank = np.zeros(current_frame.shape, dtype='uint8')
    
    # difference between frames
    frame_difference = cv.absdiff(current_frame, next_frame)
    gray_frame_difference = cv.GaussianBlur(frame_difference, (21,21), 0)
    gray_frame_difference = cv.cvtColor(gray_frame_difference, cv.COLOR_BGR2GRAY)

    
    # black and white
    retval, thresh_frame = cv.threshold(gray_frame_difference,20, 255, cv.THRESH_BINARY)
    thresh_frame = cv.dilate(thresh_frame, None, iterations=3)
    thresh_frame = cv.erode(thresh_frame, None, iterations=1)
    
    # find contours
    contours, _ = cv.findContours(thresh_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # draw only big contours filled
    for contour in contours:
        if cv.contourArea(contour) <5000:  # ignore small noise
            continue
        cv.drawContours(blank, [contour], -1, (255,255,255), -1)  # -1 = filled
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(current_frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    
    
    cv.imshow("motion detector", blank)
    cv.imshow("motion ",current_frame)
    
    current_frame = next_frame
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()