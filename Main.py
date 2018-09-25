"""
Jan Adamczyk - 2018
"""
from threading import Thread
from tkinter import Tk, Label, Entry, Button

from Graphs import Surface3D_Graph, Line2D_Graph
from TCP.TCP_Handler import TCP_Handler

tcp_Thread = Thread(target=TCP_Handler)
tcp_Thread.start()


def clicked():
    Surface3D_Graph.widthOfData = txt.get()


window = Tk()
window.title("Config")
window.geometry('350x200')
lbl = Label(window, text="Data-width")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Set", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
