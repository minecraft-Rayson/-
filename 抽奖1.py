﻿import random,time
#中文抽奖主体系
def chinesetixi():
    global chinese,language
    chinese=random.randint(1,5)
    if chinese==1:
        print("正在抽奖中……")
        time.sleep(3)
        print("奖品1")
        time.sleep(5)
        ljianc()
    elif chinese==2:
        print("正在抽奖中……")
        time.sleep(3)
        print("奖品2")
        time.sleep(5)
        ljianc()
    elif chinese==3:
        print("正在抽奖中……")
        time.sleep(3)
        print("奖品3")
        time.sleep(5)
        ljianc()
    elif chinese==4:
        print("正在抽奖中……")
        time.sleep(3)
        print("奖品4")
        time.sleep(5)
        ljianc()
    elif chinese==5:
        print("正在抽奖中……")
        time.sleep(3)
        print("奖品5")
        time.sleep(5)
        ljianc()
#中文抽奖主体系结束
#英文抽奖主体系
def englishtixi():
    global english,language
    english=random.randint(1,5)
    if english==1:
        print("Lottery is in progress...")
        time.sleep(3)
        print("prize1")
        time.sleep(5)
        ljianc()
    elif english==2:
        print("Lottery is in progress...")
        time.sleep(3)
        print("prize2")
        time.sleep(5)
        ljianc()
    elif english==3:
        print("Lottery is in progress...")
        time.sleep(3)
        print("prize3")
        time.sleep(5)
        ljianc()
    elif english==4:
        print("Lottery is in progress...")
        time.sleep(3)
        print("prize4")
        time.sleep(5)
        ljianc()
    else:
        print("Lottery is in progress...")
        time.sleep(3)
        print("prize5")
        time.sleep(5)
        ljianc()
#英语抽奖主体系结束
#语言判断主体系
def ljianc():
    global error
    language=int(input("Please select language, 1.中文,2.English,3.输入3以停止程序"))#语言选择
    if language==1:
        chinesetixi()
    elif language==3:
        print("已停止,谢谢使用")
        time.sleep(5)
    elif language==2:
        englishtixi()
    else:
        print("啊？")
        time.sleep(5)
        ljianc()
#语言判断主体系结束
print("welcome to lottery2.0")
time.sleep(5)
ljianc()#调用语言检测