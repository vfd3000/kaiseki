import pyautogui as pg
from pynput import mouse
from time import sleep
import pygetwindow as gw



#イベント検知
def on_click(x, y, button, pressed):
        if pressed:
            return False


        
#配列宣言
xaxis = []
yaxis = []
words = ["syou","tyu1","tyu2","tyu3","tyu4","tyu5","dai"]

#座標読み取り
for i in range(3):
        with mouse.Listener(on_click=on_click) as listener:
                listener.join()
                x,y=pg.position()
                xaxis.append(x)
                yaxis.append(y)

print(str(xaxis[0])+" "+str(yaxis[0]))

#数字処理
xlefttop = xaxis[0]
ylefttop = yaxis[0]
width = (xaxis[1]-xaxis[0])//4
height = (yaxis[2]-yaxis[0])//4


#editをregionに変更
with pg.hold("ctrl"):
        pg.press("r")




for i in range(4):
        
        for s in range(4):
                
                for w in words:
                        
                        image_filename = w+".png"
                        pg.doubleClick(pg.locateOnScreen("./hosi/"+image_filename,confidence=0.5,region=(xlefttop+(i*width),ylefttop+(s*height),width,height)))
                        sleep(2)

                        try:
                                window = gw.getWindowsWithTitle("Circle")[0]
                        except IndexError as e:
                                continue
                        
                        window.activate()

                        

                        


                        with pg.hold("ctrl"):
                                pg.press("w")

                        
                        
                        

                        sleep(2)

                        print(str(xlefttop+(i*width))+" "+str(ylefttop+s*height)+" "+str(width)+" "+str(height))