from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('United Kingdom BST')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('times new roman', 40, 'bold'),
              background = 'green',
              foreground = 'white')
clock.pack(anchor = 'center')
time()
mainloop()
