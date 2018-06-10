
# import libraries
from tkinter import *
import tkinter.messagebox


# Make window and set size/ title
root2 = Tk()
root2.geometry("250x280")
root2.title("A simple calculator *_*")


# Make statusbar at bottom of window
frame2 = Frame(root2, bg = "blue")
frame2.pack(side = BOTTOM, fill=X)
statusbar = Label(frame2, text="Woohoo! :)", bd = 1, relief=SUNKEN, anchor=W)
statusbar.pack(side = BOTTOM, fill=X)


# Make main frame and header
frame1 = Frame(root2, bd = 10)
frame1.pack(fill = X)

text1 = Label(frame1, text="Math is EZPZ",font = ("Courier",20), bd = 10)
text1.grid(row=1, columnspan = 3)

# Make calculator function
def sel():
	try:
		if var.get()== 1:
			ans = float(entry1.get()) + float(entry2.get())
		elif var.get()== 2:
			ans = float(entry1.get()) - float(entry2.get())
		elif var.get()== 3:
			ans = float(entry1.get()) * float(entry2.get())
		elif var.get()== 4:
			ans = float(entry1.get()) / float(entry2.get())
		if round(ans,2)==ans:
			selection = "The answer is " + str(ans)
		else:
			selection = "The answer is " + str(round(ans,2)) + " (to 2 d.p)"

		label.config(text = selection)
	except:
		selection = "Please enter a valid number"
		label.config(text = selection)

# Make entry fields for numbers
entry1 = Entry(frame1, width = 6, bd = 5)
entry1.grid(row = 2)

entry2 = Entry(frame1, width = 6, bd = 5)
entry2.grid(row = 2, column = 2)


# Make radio button options for operators
var = IntVar()
R1 = Radiobutton(frame1, text = "+", variable=var, value=1, command = sel)
R1.grid(row = 2, column = 1)

R2 = Radiobutton(frame1, text = "-", variable=var, value=2, command = sel)
R2.grid(row = 3, column = 1)

R3 = Radiobutton(frame1, text="*", variable=var, value=3, command = sel)
R3.grid(row = 4,column = 1)

R4 = Radiobutton(frame1, text="/", variable=var, value=4, command = sel)
R4.grid(row = 5,column = 1)

show = Button(frame1, text="Solve it!", bd = 10,command = sel)
show.grid(row = 6, column = 1)

label = Label(frame1, bd =8)
label.grid(row=8, columnspan = 3)

root2.mainloop()


