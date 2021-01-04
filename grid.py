from tkinter import *

root = Tk()

# lable widget
mylable1 =Label(root, text="hello world!")
mylable2 =Label(root, text="hello world!")

# grid
mylable1.grid(row=0, column=0)
mylable2.grid(row=1, column=2)

# # show to screen
# mylable1.pack()
# mylable2.pack()

root.mainloop()

