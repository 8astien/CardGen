import tkinter
from tkinter import *
import mainScript

descFont = 'ressources/Roboto-Regular.ttf', 12

window = Tk() #create a window

# add widgets here

btn = Button(window, text = "Ok", fg = 'black', font = descFont)
btn.place(x=900, y=50)
lbl = Label(window, text = "Card Name", fg = 'black', font = descFont)
lbl.place(x=450, y=50)
txtfld = Entry(window, text="", bd=5)
txtfld.place(x=600, y=50)


window.title('CardGen pre-release version 0.000000000432')
window.geometry("1024x720+10+20")
window.mainloop() #mainloop displays the window
