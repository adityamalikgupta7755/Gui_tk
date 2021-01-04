from tkinter import *

root = Tk()

def myclick():
    mylable = Label(root, text=" cool amg")
    mylable.pack()



# mybtn = Button(root, text="submit", state=DISABLED)
# mybtn = Button(root, text="submit", padx=50 ,pady=25)
mybtn = Button(root, text="submit",command=myclick, fg="blue", bg="red")
mybtn.pack()
# mybtn.grid(row =0 ,column = 1)
root.mainloop()

