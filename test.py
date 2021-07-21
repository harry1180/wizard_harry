from tkinter import *
from PIL import ImageTk ,Image
import tkinter as tk
import ui
base = Tk()
base.title('Start Button')

img=ImageTk.PhotoImage(Image.open ("welcome1.jfif"))
lab=Label(image=img)
#lab.pack()
lab.pack(fill=tk.BOTH, expand=1)
def greet():
    return 'hello world'
#button=Button(base,text='exit',command=base.quit)
button=Button(base,text='exit',command=greet())
button.pack()
#button1.pack()
base.mainloop()
