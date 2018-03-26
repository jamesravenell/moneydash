import tkinter as tk
from tkinter import ttk  #this is needed for the Label

win = tk.Tk()
name = tk.Tk()
win.title('Get That Dough!')

#Modify adding a Label
aLabel = ttk.Label(win,text = 'This is a Label')
aLabel.grid(column=0, row=0)

#Button Click Event funtion
def clickMe():
    action.configure(text='Wassup ' + name())
    # action.configure(text="**I Have Been CLICKED!**")
    # aLabel.configure(foreground='Red')
    # aLabel.configure(text='A Red Label')

#Changing our aLabel
ttk.Label(win,text='Enter a name: ').grid(column=0,row=0)

#Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=20, textvariable = name)
nameEntered.grid(column=1,row=0)

#Adding a Button
action = ttk.Button(win,text='Click Me!', command=clickMe)
action.grid(column=0, row=2)


# win.resizable(0,900)
win.mainloop() #GUI won't start until this line is executed
