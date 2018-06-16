import tkinter as Tkinter
import DotModel as Model

root = Tkinter.Tk()
model= Model.DotModel()

def key(event):
    print ("pressed"), repr(event.char)

def callback(event):
    print ("clicked at"), event.x, event.y

def mouseMove(event):
    print("The coord x=",event.x," The Y coord =",event.y)

canvas= Tkinter.Canvas(root, width=500, height=500)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.bind('<Motion>',mouseMove)
canvas.pack()

root.mainloop()