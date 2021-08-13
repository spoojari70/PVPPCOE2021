
import tkinter
from tkinter import *
import tkinter.messagebox



App = tkinter.Tk()

def MyMessage():
    return tkinter.messagebox.showinfo("Button clicked successfully ")

clickbtn = tkinter.Button(App,text ="Click here", bg= "Red",commmand = MyMessage)
clickbtn.pack()

App.mainloop()