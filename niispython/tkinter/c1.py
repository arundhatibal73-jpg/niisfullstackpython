from tkinter import *

root = Tk()
root.title("Calculator")

def add():
    result.set(int(e1.get()) + int(e2.get()))

e1 = Entry(root)
e1.grid(row=0, column=1)

e2 = Entry(root)
e2.grid(row=1, column=1)

Label(root, text="Num1").grid(row=0)
Label(root, text="Num2").grid(row=1)

result = StringVar()

Button(root, text="Add", command=add).grid(row=2, column=0)

Label(root, textvariable=result).grid(row=2, column=1)

root.mainloop()