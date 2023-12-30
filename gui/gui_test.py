from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your Name!")


def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()


# , state=WRITABLE, fg="blue", bg="#ffffff", padx=50, pady=50
myButton = Button(root, text="Enter Your Name!", command=myClick)

myButton.pack()

root.mainloop()
