import Tkinter as tk

def changeColour():
    label = tk.Label(master, text="TEXT", fg=textColour)
    print "Zmieniono na " + textColour

def setColour(colour):
    textColour = colour

master = tk.Tk()
textColour = "black"

label = tk.Label(master, text="TEXT", fg="black").grid(column=0, row=0)

v = tk.IntVar()
tk.Radiobutton (master,
                text = "RED",
                variable = v,
                command = setColour("red"),
                value = 1).grid(column=0, row=1)

tk.Radiobutton (master,
                text = "BLUE",
                variable = v,
                command = setColour("blue"),
                value = 2).grid(column=0, row=2)

tk.Radiobutton (master,
                text = "GREEN",
                variable = v,
                command = setColour("green"),
                value = 3).grid(column=0, row=3)

b = tk.Button(text="Change Colour", command = lambda:changeColour()).grid(column=0, row=4)

master.mainloop()
