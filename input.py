from tkinter import *

root = Tk()

# input field
# entry =Entry(root, width=50, bg="blue",fg="white")
entry =Entry(root, width=50,)
entry.pack()
entry.insert(0, "enter your name :-")



def myclick():
    h ="hello "+entry.get()
    mylable = Label(root, text=h)
    mylable.pack()



# mybtn = Button(root, text="submit", state=DISABLED)
# mybtn = Button(root, text="submit", padx=50 ,pady=25)
mybtn = Button(root, text="enter name",command=myclick)
mybtn.pack()
# mybtn.grid(row =0 ,column = 1)
root.mainloop()

