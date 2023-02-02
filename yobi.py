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
words = ["syou","tyu","dai"]

#座標読み取り
for i in range(3):
        with mouse.Listener(on_click=on_click) as listener:
                listener.join()
                x,y=pg.position()
                xaxis.append(x)
                yaxis.append(y)

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
                        sleep(3)
                        pg.click(pg.locateOnScreen("./iroiro/apply.png",confidence=0.6))
                        
                        try:
                                window = gw.getWindowsWithTitle("Circle")[0]
                        except IndexError as e:
                                continue
                        
                        window.activate()
                        cx,cy=window.topleft
                        cwidth,cheight=window.size

                        pg.click(pg.locateOnScreen("./iroiro/Analysis.png",confidence=0.6,region=(cx,cy,cwidth,cheight)))
                        sleep(3)
                        pg.click(pg.locateOnScreen("./iroiro/plot3d.png",confidence=0.6))

                        sleep(3)
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

                        sleep(3)
                
                


#同じはんいを選択してしまったときのこと考える 