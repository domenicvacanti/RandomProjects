import tkinter as tk
import time

def startTime():
    global start
    start = time.time()
    label0["text"] = "Started"
    startTimeButton["text"] = "Start New Game"
    label1["text"] = "Flash Up"
    label2["text"] = "Flash Up"
    label3["text"] = "Flash Up"
    label4["text"] = "Flash Up"
    label5["text"] = "Flash Up"
    

def flashInc1():
    get1 = time.time()
    passedTime = get1 - start
    passedTime = get1 - start + 300
    minutes, seconds = divmod(passedTime, 60)
    seconds = int(seconds)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    label1["text"] = "{}:{}".format(int(minutes),seconds)

def flashInc2():
    get = time.time()
    passedTime = get - start + 300
    minutes, seconds = divmod(passedTime, 60)
    seconds = int(seconds)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    label2["text"] = "{}:{}".format(int(minutes),seconds)
def flashInc3():
    get = time.time()
    passedTime = get - start + 300
    minutes, seconds = divmod(passedTime, 60)
    seconds = int(seconds)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    label3["text"] = "{}:{}".format(int(minutes),seconds)
def flashInc4():
    get = time.time()
    passedTime = get - start + 300
    minutes, seconds = divmod(passedTime, 60)
    seconds = int(seconds)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    label4["text"] = "{}:{}".format(int(minutes),seconds)
def flashInc5():
    get = time.time()
    passedTime = get - start + 300
    minutes, seconds = divmod(passedTime, 60)
    seconds = int(seconds)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    label5["text"] = "{}:{}".format(int(minutes),seconds)

window = tk.Tk()
window.title("League of Legends Flash Timer")
window.resizable(width=False,height=False)
frame0 = tk.Frame()
frame0.pack(fill=tk.Y)
frame1 = tk.Frame()
frame1.pack(fill=tk.Y)
frame2 = tk.Frame()
frame2.pack(fill=tk.Y)
frame3 = tk.Frame()
frame3.pack(fill=tk.Y)
frame4 = tk.Frame()
frame4.pack(fill=tk.Y)
frame5 = tk.Frame()
frame5.pack(fill=tk.Y)
frame6 = tk.Frame()
frame6.pack(fill=tk.Y)

playerBanner = tk.Label(master= frame1, text="Players")
playerBanner.pack(side=tk.LEFT)
player1Banner = tk.Label(master= frame2, text="TOP")
player1Banner.pack(side=tk.LEFT)
player2Banner = tk.Label(master= frame3, text="JNG")
player2Banner.pack(side=tk.LEFT)
player3Banner = tk.Label(master= frame4, text="MID")
player3Banner.pack(side=tk.LEFT)
player4Banner = tk.Label(master= frame5, text="ADC")
player4Banner.pack(side=tk.LEFT)
player5Banner = tk.Label(master= frame6, text="SUP")
player5Banner.pack(side=tk.LEFT)

startTimeButton = tk.Button(master=frame1,text="Begin Game",command=startTime)
startTimeButton.pack(side=tk.LEFT)
player1Sum1 = tk.Button(master=frame2, text="Flash",command=flashInc1)
player1Sum1.pack(side=tk.LEFT)
player2Sum1 = tk.Button(master=frame3, text="Flash",command=flashInc2)
player2Sum1.pack(side=tk.LEFT)
player3Sum1 = tk.Button(master=frame4, text="Flash",command=flashInc3)
player3Sum1.pack(side=tk.LEFT)
player4Sum1 = tk.Button(master=frame5, text="Flash",command=flashInc4)
player4Sum1.pack(side=tk.LEFT)
player5Sum1 = tk.Button(master=frame6, text="Flash",command=flashInc5)
player5Sum1.pack(side=tk.LEFT)

label0 = tk.Label(master=frame1, text="Not Started")
label0.pack(side=tk.LEFT)
label1 = tk.Label(master=frame2, text="Flash Up")
label1.pack(side=tk.LEFT)
label2 = tk.Label(master=frame3, text="Flash Up")
label2.pack(side=tk.LEFT)
label3 = tk.Label(master=frame4, text="Flash Up")
label3.pack(side=tk.LEFT)
label4 = tk.Label(master=frame5, text="Flash Up")
label4.pack(side=tk.LEFT)
label5 = tk.Label(master=frame6, text="Flash Up")
label5.pack(side=tk.LEFT)

window.mainloop()
