import tkinter

import tkinter.ttk

App = tkinter.Tk()

Pb = tkinter.ttk.Progressbar(orient = "vertical",length = 10 )
Pb.pack()

App.mainloop()