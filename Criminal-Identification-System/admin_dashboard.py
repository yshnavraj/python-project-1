from tkinter import *
from tkinter import ttk
import tkinter
window = Tk()
window.title("Admin Dashboard")
window.geometry('800x600')
# window.configure(background = "grey");

T = tkinter.Label(window, text="Adding Police 1", font = ("Times", 20, "bold italic")).grid(row = 0, column = 0)



a = Label(window ,text = "First Name").grid(row = 1,column = 0)
b = Label(window ,text = "Last Name").grid(row = 2,column = 0)
c = Label(window ,text = "Email Id").grid(row = 3,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 4,column = 0) 
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=5,column=0)
window.mainloop()
