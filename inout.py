from ast import Delete
import itertools
from tkinter import *
import tkinter as tk
import os




window=tk.Tk()
window.title(" InOutput Desktop App ")
window.geometry("600x400")

path = 'D:\BK COURSE\HK212\PPL\Assignment\Assignment2\initial\src\\test\\'

def onSelect(evt):
    selected = evt.widget.get(evt.widget.curselection())
    inputFile = open( path + 'testcases\\' + selected, 'r')
    data = inputFile.read()
    inputtxt.delete("1.0", "end")
    inputtxt.insert(tk.END, data)

    outputFile = open( path + 'solutions\\' + selected, 'r')
    Output.delete("1.0", "end")
    data = outputFile.read()
    Output.insert(tk.END, data)

    


##Scroll Bar Initializes
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )




myList = os.listdir(path + 'solutions')
button =  Listbox(window, yscrollcommand=scrollbar.set)
counter = itertools.count(0)
[button.insert(END, filename) for filename in myList]

button.bind('<<ListboxSelect>>', onSelect)

button.pack(side=LEFT, fill=BOTH)   
scrollbar.config(command=button.yview)
# [b.pack() for b in button]
##Display
l = Label(text="Input")
inputtxt = Text(window, height=10,
                width=200,
                bg="light yellow")
out = Label(text="Output")
Output = Text(window, height=10,
              width=200, 
              bg="light cyan")
l.pack()
inputtxt.pack()
out.pack()
Output.pack()

## Insert data



window.mainloop()
