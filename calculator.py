from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
e = Entry(root, width=30)
e.grid(padx=30, pady=10, columnspan=4)


def click_btn(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n))


def del_btn():
    e.delete(0, END)


def plus_btn():
    global num_one
    global act
    num_one = int(e.get())
    act = "plus"
    e.delete(0, END)


def minus_btn():
    global num_one
    global act
    num_one = int(e.get())
    act = "minus"
    e.delete(0, END)


def multiply_btn():
    global num_one
    global act
    num_one = int(e.get())
    act = "multiply"
    e.delete(0, END)


def chastnoe():
    global num_one
    global act
    num_one = int(e.get())
    act = "chastnoe"
    e.delete(0, END)


def ostatok():
    global num_one
    global act
    num_one = int(e.get())
    act = "ostatok"
    e.delete(0, END)


def equal():
    num_two = int(e.get())
    e.delete(0, END)
    if act == "plus":
        e.insert(0, num_one + num_two)
    if act == "minus":
        e.insert(0, num_one - num_two)
    if act == "multiply":
        e.insert(0, num_one * num_two)
    if act == "chastnoe":
        e.insert(0, num_one // num_two)
    if act == "ostatok":
        e.insert(0, num_one % num_two)


btn_delost = ttk.Button(width=15, text="//", command=chastnoe)
btn_delbezost = ttk.Button(width=15, text="%", command=ostatok)
btn_1 = ttk.Button(text="1", command=lambda: click_btn(1))
btn_2 = ttk.Button(text="2", command=lambda: click_btn(2))
btn_3 = ttk.Button(text="3", command=lambda: click_btn(3))
btn_4 = ttk.Button(text="4", command=lambda: click_btn(4))
btn_5 = ttk.Button(text="5", command=lambda: click_btn(5))
btn_6 = ttk.Button(text="6", command=lambda: click_btn(6))
btn_7 = ttk.Button(text="7", command=lambda: click_btn(7))
btn_8 = ttk.Button(text="8", command=lambda: click_btn(8))
btn_9 = ttk.Button(text="9", command=lambda: click_btn(9))
btn_0 = ttk.Button(width=17, text="0", command=lambda: click_btn(0))
btn_Clear = ttk.Button(width=6, text="CLEAR", command=del_btn)
btn_equal = ttk.Button(text="=", command=equal)
btn_plus = ttk.Button(text="+", command=plus_btn)
btn_minus = ttk.Button(text="-", command=minus_btn)
btn_multiply = ttk.Button(width=6, text="*", command=multiply_btn)

btn_delost.grid(columnspan=2, padx=2, pady=10, column=0, row=1)
btn_delbezost.grid(columnspan=2, padx=2, pady=10, column=2, row=1)
btn_0.grid(columnspan=2, padx=2, pady=10, column=0, row=5)
btn_1.grid(padx=2, pady=10, column=0, row=2)
btn_2.grid(padx=2, pady=10, column=1, row=2)
btn_3.grid(padx=2, pady=10, column=2, row=2)
btn_4.grid(padx=2, pady=10, column=0, row=3)
btn_5.grid(padx=2, pady=10, column=1, row=3)
btn_6.grid(padx=2, pady=10, column=2, row=3)
btn_7.grid(padx=2, pady=10, column=0, row=4)
btn_8.grid(padx=2, pady=10, column=1, row=4)
btn_9.grid(padx=2, pady=10, column=2, row=4)
btn_plus.grid(padx=6, pady=10, column=3, row=3)
btn_Clear.grid(columnspan=1, padx=0, pady=10, column=2, row=5)
btn_equal.grid(padx=6, pady=10, column=3, row=5)
btn_minus.grid(padx=6, pady=10, column=3, row=2)
btn_multiply.grid(padx=6, pady=10, column=3, row=4)

root.mainloop()
