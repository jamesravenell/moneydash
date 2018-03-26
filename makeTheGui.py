import tkinter as tk
from tkinter import ttk  #this is needed for the Label

win = tk.Tk()
win.title('Get That Dough!')

#Modify adding a Label
aLabel = ttk.Label(win,text = 'This is a Label')
aLabel.grid(column=0, row=0)

#Button Click Event funtion
def clickMe():
    action.configure(text="**I Have Been CLICKED!**")
    aLabel.configure(foreground='Red')
    aLabel.configure(text='A Red Label')


#Adding a Button
action = ttk.Button(win,text='Click Me Fool!', command=clickMe)
action.grid(column=1, row=0)


# win.resizable(0,900)
win.mainloop() #GUI won't start until this line is executed
