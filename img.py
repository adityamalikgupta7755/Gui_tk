from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aditya")
root.iconbitmap('a.ico')


my_img = ImageTk.PhotoImage(Image.open("pic.png"))
my_lable = Label(image=my_img)
my_lable.pack()

btn_quit = Button(root, text="exit", command=root.quit)
btn_quit.pack()

root.mainloop()