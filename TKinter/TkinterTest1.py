from Tkinter import *

def doButtonMain(bttnNum):
	tempText = myLabel.cget("text")
	myLabel.configure(text=str(tempText)+"\n"+"You have Clicked Button " + str(bttnNum))

def doButton1():
	doButtonMain(1)

def doButton2():
	doButtonMain(2)

def doButton3():
	doButtonMain(3)

def doButton4():
	doButtonMain(4)

def doButton5():
	doButtonMain(5)

def doButton6():
	doButtonMain(6)

mw = Tk()

myLabel = Label(mw)
myLabel.grid(row=0, column=1, rowspan=3, columnspan=1)

b1 = Button(mw, text="A", command=doButton1)
b1.grid(row=0, column=0)

b2 = Button(mw, text="B", command=doButton2).grid(row=1, column=0)

b3 = Button(mw, text="C", command=doButton3)
b3.grid(row=2, column=0)

b4 = Button(mw, text="D", command=doButton4)
b4.grid(row=0, column=3)

b5 = Button(mw, text="E", command=doButton5)
b5.grid(row=1, column=3)

b6 = Button(mw, text="F", command=doButton6)
b6.grid(row=2, column=3)

mainloop()
