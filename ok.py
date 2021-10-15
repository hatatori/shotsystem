
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while True:
    img_rgb = ImageGrab.grab(bbox=(0,0,1366,720))
    img_rgb = np.array(img_rgb)

    template = cv2.imread('imgs/alvo2.png',0)

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    w = template.shape[1]
    h = template.shape[0]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where( res >= threshold)
    
    # se aparece na tela
    if(len(loc[0] > 0)):

        x = np.asarray(loc[1])[0]
        y = np.asarray(loc[0])[0]

        rec = cv2.rectangle(img_rgb, (x+w,y+h),(x,y), (0,0,255), 2)

        # click(int((x+w)/2),int((y+h)/2))
        click(x+15,y+15)

    if cv2.waitKey(33) & 0xFF in (
        ord('q'), 
        27, 
    ):
        break

cv2.waitKey()
cv2.destroyAllWindows()
##http://www.aimbooster.com/