from Tkinter import *

showing = True

def show():
	global showing
	if showing:
		myFrame.grid_remove()
		ShowButton.configure(text="Show")
		showing = False
	else:
		myFrame.grid()
		ShowButton.configure(text="HIDE")
		showing = True
	
def update_label():
	Label1.configure(text=str(myScale.get()))

mw = Tk()

ShowButton = Button(mw, text="HIDE", command=show)
ShowButton.grid(row = 0, column = 0)

myFrame = Frame(mw)
myFrame.grid(row=1,column=0,rowspan=3)

Label1 = Label(myFrame, text="hi")
Label1.grid(row = 1, column = 0)

myScale = Scale(myFrame, from_=0, to=100, orient=HORIZONTAL)
myScale.grid(row = 2, column = 0)

while True:
	mw.update()
	update_label()
