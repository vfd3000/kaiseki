import pyautogui as pg
from pynput import mouse
from time import sleep
import pygetwindow as gw
from PIL import Image




def on_click(x, y, button, pressed):
        if pressed:
            return False


        
words = ["syou","tyu1","tyu2","tyu3","tyu4","tyu5","dai"]
xaxis = []
yaxis = []

for i in range(3):
        with mouse.Listener(on_click=on_click) as listener:
                listener.join()
                x,y=pg.position()
                xaxis.append(x)
                yaxis.append(y)

xlefttop = xaxis[0]
ylefttop = yaxis[0]
width = (xaxis[1]-xaxis[0])//4
height = (yaxis[2]-yaxis[0])//4

with pg.hold("ctrl"):
        pg.press("r")




for i in range(4):
        
        for s in range(4):
                
                for w in words:
                        
                        image_filename = w+".png"
                        pg.doubleClick(pg.locateOnScreen("hosi/"+image_filename,confidence=0.5,region=(xlefttop+(i*width),ylefttop+(s*height),width,height)))
                        sleep(1)