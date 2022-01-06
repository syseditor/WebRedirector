from tkinter import *
import webbrowser

def func():
    webbrowser.open_new_tab(e1.get())
    root.destroy()

def clear():
    e1.delete(0, 100)

root = Tk()
root.title("Web Redirector")

e1 = Entry(root).grid(row=2, column=1, sticky=W)
b1 = Button(root, text="Search", fg="green", bg="black", command=func).grid(row=3, column=1, sticky=W)
b2 = Button(root, text="Clear", fg="red", bg="black", command=clear).grid(row=4, column=1, sticky=W)

root.mainloop()
