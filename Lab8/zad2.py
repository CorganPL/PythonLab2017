from Tkinter import *
import time

def countdown(seconds):
    while (seconds>=0):
        time.sleep(1)
        timeLabel.config(text=seconds)
        seconds-=1
        if (seconds == 0):
            print "Zakonczono odliczanie"

master = Tk()
seconds = 5
timeLabel = Label(master, text=seconds)
timeLabel.grid(row=0)

b1 = Button(master, text="START", command = lambda: countdown(seconds))
b1.grid(row=1)

master.mainloop()
