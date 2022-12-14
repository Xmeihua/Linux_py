import tkinter
import threading
import datetime
import time

app=tkinter.Tk()
app.overrideredirect(True)         #不显示标题栏
app.attributes('-alpha',0.9)       #半透明
app.attributes('-topmost',1)       #总是在顶端
app.geometry('130*25+100+100')     #初始大小与位置

labelDateTime=tkinter.Label(app,width=130) #显示时间的标签
labelDateTime.pack(fill=tkinter.BOTH,expand=tkinter.YES)
labelDateTime.configure(bg='gray')

X=tkinter.IntVar(value=0)          #记录鼠标健按下的位置
Y=tkinter.IntVar(value=0)
canMove=tkinter.IntVar(value=0)    #窗口是否可托动
still=tkinter.IntVar(value=1)      #是否仍在运行

def onLeftButtonDown(event):
    app.attributes('-alpha',0.4)   #开始托动时增加透明度
    X.set(event.x)                 
    Y.set(event.y)
    canMove.set(1)
labelDateTime.bind('<Button-1>',onLeftButtonDown)
def onLeftButtonup(event):
    app.attributes('-alpha',0.9)
    canMove(0)
labelDateTime.bind('<ButtonRelease-1>',onLeftButtonup)

def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    newX=app.winfo_x()+(event.x-X.get())
    newY=app.winfo_y()+(event.y-Y.get())
    g='130*25'+str(newX)+'+'+str(newY)
    app.geometry(g)
labelDateTime.bind('<B1-Motion>',onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    still.join(0.2)
    app.destroy()
labelDateTime.bind('<Button-3>',onRightButtonDown)
def nowDateTime():
    while still.get()==1:
        s=str(datetime.datetime.now())[:19]
        labelDateTime['text'] = s
        time.sleep(0.2)
t=threading.Thread(target=nowDateTime)
t.daemon = True
t.start()

app.mainloop()
