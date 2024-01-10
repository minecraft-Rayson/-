from tkinter import *
import random,time
def choujiang():
    global num1
    num1=random.randint(1,5)
    if num1==1:
        for i in range(1,6):
            time.sleep(2)
            print(i)
        print("奖品1")
    elif num1==2:
        for i in range(1,6):
            time.sleep(2)
            print(i)
        print("奖品2")
    elif num1==3:
        for i in range(1,6):
            time.sleep(2)
            print(i)
        print("奖品3")
    elif num1==4:
        for i in range(1,6):
            time.sleep(2)
            print(i)
        print("奖品4")
    elif num1==5:
        for i in range(1,6):
            time.sleep(2)
            print(i)
        print("奖品5")
root = Tk()
root.geometry("162x59+374+182")
root.title("666")
button = Button(root,text="按下抽奖",font=("仿宋",25),fg="blue",command=choujiang)
button.grid(row=1,column=1)
root.mainloop()