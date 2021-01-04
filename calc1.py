from tkinter import *
 
root = Tk()
root.title("Calculator")

e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10,pady=10)


def button_opt(number):
    cr=e.get()
    e.delete(0, END)
    e.insert(0, str(cr)+str(number))

def button_clear():
    e.delete(0, END)

def button_add():
   first_number = e.get()
   global f_num
   global Opreation
   Opreation ="add"
   f_num = int(first_number)
   e.delete(0, END)

def button_sub():
   first_number = e.get()
   global f_num
   global Opreation
   Opreation ="sub"
   f_num = int(first_number)
   e.delete(0, END)

def button_multi():
   first_number = e.get()
   global f_num
   global Opreation
   Opreation ="multi"
   f_num = int(first_number)
   e.delete(0, END)

def button_divid():
    first_number = e.get()
    global f_num
    global Opreation
    Opreation ="divid"
    f_num = int(first_number)
    e.delete(0, END)

def button_equl():
    second_number = e.get()
    e.delete(0, END)

    if Opreation == "add":
        e.insert(0, f_num + int(second_number))
    if Opreation == "sub":
        e.insert(0, f_num - int(second_number))
    if Opreation == "multi":
        e.insert(0, f_num * int(second_number))
    if Opreation == "divid":
        e.insert(0, f_num / int(second_number))
# creat btn
button_1 = Button(root, text="1", padx=40 ,pady=20, command=lambda:button_opt(1))
button_2 = Button(root, text="2", padx=40 ,pady=20, command=lambda:button_opt(2))
button_3 = Button(root, text="3", padx=40 ,pady=20, command=lambda:button_opt(3))
button_4 = Button(root, text="4", padx=40 ,pady=20, command=lambda:button_opt(4))
button_5 = Button(root, text="5", padx=40 ,pady=20, command=lambda:button_opt(5))
button_6 = Button(root, text="6", padx=40 ,pady=20, command=lambda:button_opt(6))
button_7 = Button(root, text="7", padx=40 ,pady=20, command=lambda:button_opt(7))
button_8 = Button(root, text="8", padx=40 ,pady=20, command=lambda:button_opt(8))
button_9 = Button(root, text="9", padx=40 ,pady=20, command=lambda:button_opt(9))
button_0 = Button(root, text="0", padx=40 ,pady=20, command=lambda:button_opt(0))


button_add = Button(root, text="+", padx=39 ,pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40 ,pady=20, command=button_sub)
button_multi = Button(root, text="*", padx=40 ,pady=20, command=button_multi)
button_divid = Button(root, text="/", padx=40 ,pady=20, command=button_divid)
button_equl = Button(root, text="=", padx=40 ,pady=20, command=button_equl)
button_clear = Button(root, text="C", padx=39 ,pady=20, command=button_clear)

# pass to screen
button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

button_0.grid(row=4 , column=0)

button_add.grid(row=2 , column=3)
button_sub.grid(row=3 , column=3)
button_multi.grid(row=4 , column=1)
button_divid.grid(row=4 , column=2)
button_equl.grid(row=4 , column=3)
button_clear.grid(row=1 , column=3)

# button_1 = Button(root, text="1", padx=40 ,pady=20, command=button_add)


# button = Button(root, text="1", padx=40 ,pady=20, command=button_add)

root.mainloop()