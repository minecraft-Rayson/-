import tkinter
from tkinter import *
import random,time
def choujiang():
    global num1,lbl
    num1=random.randint(1,5)
    if num1==1:
        lbl = Label(root, text="奖品1",font=("仿宋", 50))
        lbl.grid()
        tkinter.init()
    elif num1==2:
        lbl = Label(root, text="奖品2",font=("仿宋", 50))
        lbl.grid()
        tkinter.init()
    elif num1==3:
        lbl = Label(root, text="奖品3",font=("仿宋", 50))
        lbl.grid()
        tkinter.init()
    elif num1==4:
        lbl = Label(root, text="奖品4",font=("仿宋", 50))
        lbl.grid()
        tkinter.init()
    elif num1==5:
        lbl = Label(root, text="奖品5",font=("仿宋", 50))
        lbl.grid()
        tkinter.init()
root = Tk()
root.geometry("500x500+374+182")
root.title("抽奖赢好运")
button = Button(root,text="按下抽奖",font=("仿宋",25),fg="blue",command=choujiang)
button.grid(row=1,column=1)
root.mainloop()