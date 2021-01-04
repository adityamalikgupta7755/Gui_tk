from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aditya")
root.iconbitmap('pic/a.ico')


my_img1 = ImageTk.PhotoImage(Image.open("pic/pic1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("pic/pic2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("pic/pic3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("pic/pic4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("pic/pic5.png"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


status = Label(root, text="image 1 of "+ str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)

my_lable = Label(image=my_img1)
my_lable.grid(row =0, column=0, columnspan=3)

def next(n):
    global my_lable
    global btn_next
    global btn_pre
    my_lable.grid_forget()
    my_lable = Label(image=img_list[n-1])
    btn_next = Button(root,text=">>", command=lambda : next(n+1))
    btn_pre = Button(root, text="<<", command=lambda : pre(n-1))

    if n ==5:
        btn_next=Button(root,text=">>", state=DISABLED)


    btn_next.grid(row =1, column=2)
    btn_pre.grid(row =1, column=0)
    my_lable.grid(row =0, column=0, columnspan=3)
    # update status bar
    status = Label(root, text="image "+str(n)+" of "+ str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)
    status.grid(row =2, column=0, columnspan=3, sticky=W+E, padx=5)

def pre(n):
    global my_lable
    global btn_next
    global btn_pre

    my_lable.grid_forget()
    my_lable = Label(image=img_list[n-1])
    btn_next = Button(root,text=">>", command=lambda : next(n+1))
    btn_pre = Button(root, text="<<", command=lambda : pre(n-1))

    if n ==1:
        btn_pre=Button(root,text="<<", state=DISABLED)

    btn_next.grid(row =1, column=2)
    btn_pre.grid(row =1, column=0)
    my_lable.grid(row =0, column=0, columnspan=3)
     # update status bar
    status = Label(root, text="image "+str(n)+" of "+ str(len(img_list)),bd=1, relief=SUNKEN, anchor=E)
    status.grid(row =2, column=0, columnspan=3, sticky=W+E, padx=5)



btn_pre = Button(root, text="<<", state=DISABLED)
btn_quit = Button(root, text="exit", command=root.quit)
btn_next = Button(root, text=">>", command=lambda : next(2))

btn_pre.grid(row =1, column=0)
btn_quit.grid(row =1, column=1)
btn_next.grid(row =1, column=2, pady=10)
status.grid(row =2, column=0, columnspan=3, sticky=W+E, padx=5)


root.mainloop()