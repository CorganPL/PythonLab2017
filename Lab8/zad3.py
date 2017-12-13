from Tkinter import *

def ref(x):
    global operation
    operation += x

master = Tk()

operation = ""
operationLabel = Label(master, text="")
operationLabel.grid(row=0)

resultLabel = Label(master, text="")
resultLabel.grid(row=0)


b1 = Button(master, text="1", command = lambda: ref(1))
b1.grid(row=0, column=0)
b2 = Button(master, text="2", command = lambda: ref(2))
b2.grid(row=0, column=1)
b3 = Button(master, text="3", command = lambda: ref(3))
b3.grid(row=0, column=2)
b4 = Button(master, text="4", command = lambda: ref(4))
b4.grid(row=1, column=0)
b5 = Button(master, text="5", command = lambda: ref(5))
b5.grid(row=1, column=1)
b6 = Button(master, text="6", command = lambda: ref(6))
b1.grid(row=1, column=2)
b7 = Button(master, text="7", command = lambda: ref(7))
b1.grid(row=2, column=0)
b8 = Button(master, text="8", command = lambda: ref(8))
b1.grid(row=2, column=1)
b9 = Button(master, text="9", command = lambda: ref(9))
b1.grid(row=2, column=2)
b0 = Button(master, text="0", command = lambda: ref(0))
b1.grid(row=3, column=1)

badd = Button(master, text="+", command = lambda: ref("+"))
badd.grid(row=4, column=0)
bsub = Button(master, text="-", command = lambda: ref(1))
bsub.grid(row=4, column=1)
bmul = Button(master, text="x", command = lambda: countdown(seconds))
bmul.grid(row=4, column=2)
bdiv = Button(master, text="/", command = lambda: countdown(seconds))
bdiv.grid(row=5, column=1)
bequal = Button(master, text="=", command = lambda: countdown(seconds))
bequal.grid(row=5, column=2)

master.mainloop()
