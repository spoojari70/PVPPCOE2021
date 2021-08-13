
import tkinter
from tkinter import messagebox

app = tkinter.Tk()
def Display():
    messagebox.showinfo("Hi Everone ",message= "Need coffee urgently")
CLICK_BUTTON = tkinter.Button(app, text="HEY I AM A BUTTON", bg="red", command=Display)
CLICK_BUTTON.pack()
app.mainloop()


