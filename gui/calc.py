from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    if number < 0 or number > 9:
        e.delete(0, END)
    e.insert(END, number)


def button_click_add(char):
    first_number = e.get()
    global f_num
    global math
    math = char
    f_num = float(first_number)
    button_clear()


def button_click_equ():
    second_number = e.get()
    number = 0
    e.delete(0, END)
    if math == '+':
        number = f_num + int(second_number)
    elif math == '-':
        number = f_num - int(second_number)
    elif math == '*':
        number = f_num * int(second_number)
    elif math == '/':
        number = f_num / int(second_number)
    e.insert(0, str(number))


def button_clear():
    e.delete(0, END)


# define buttons
button_1 = Button(root, text="1", width=20, height=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=20, height=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=20, height=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=20, height=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=20, height=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=20, height=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=20, height=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=20, height=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=20, height=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=20, height=5, command=lambda: button_click(0))
button_add = Button(root, text="+", width=20, height=5, command=lambda: button_click_add('+'))
button_equ = Button(root, text="=", width=41, height=5, command=button_click_equ)
button_clr = Button(root, text="Clear", width=41, height=5, command=button_clear)

button_sub = Button(root, text="-", width=20, height=5, command=lambda: button_click_add('-'))
button_mul = Button(root, text="*", width=20, height=5, command=lambda: button_click_add('*'))
button_div = Button(root, text="/", width=20, height=5, command=lambda: button_click_add('/'))

# put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1, columnspa=2)
button_add.grid(row=5, column=0)
button_equ.grid(row=5, column=1, columnspa=2)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

# , state=WRITABLE, fg="blue", bg="#ffffff", padx=50, pady=50


root.mainloop()
