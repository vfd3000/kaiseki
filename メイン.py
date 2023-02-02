import pyautogui as pg
from pynput import mouse
from time import sleep
import pygetwindow as gw




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
                        pg.doubleClick(pg.locateOnScreen("./hosi/"+image_filename,confidence=0.5,region=(xlefttop+(i*width),ylefttop+(s*height),width,height)))
                        sleep(1)
                        
                        
                        try:
                                window = gw.getWindowsWithTitle("Circle")[0]
                        except IndexError as e:
                                continue
                        
                        window.activate()
                        cx,cy=window.topleft
                        cwidth,cheight=window.size
                        sleep(1)

                        pg.click(pg.locateOnScreen("./iroiro/Analysis.png",confidence=0.6,region=(cx,cy,cwidth,cheight)))
                        sleep(1)
                        pg.click(pg.locateOnScreen("./iroiro/plot3d.png",confidence=0.6))

                        sleep(1)
#グラフ保存
                        window = gw.getWindowsWithTitle("Circle")[0]
                        window.activate()
                        cx,cy=window.topleft
                        cwidth,cheight=window.size


#グラフの名前は何回目のループか、またほしの輝きの強さでわける
                        filename=str(i)+str(s)+w+".png"

                        pg.screenshot('./Image/'+filename,region=(cx,cy,cwidth,cheight))
        
                        with pg.hold("ctrl"):
                                pg.press("w")
        
                        with pg.hold("ctrl"):
                                pg.press("w")

                        sleep(1)
                
                

#次回やることメモ
#なんも検出しなかった時の処理考える try except
#同じはんいを選択してしまったときのこと考える 




