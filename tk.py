from tkinter import *
from infix import *
a=prefixfunction("a*b")
root=Tk()
root.geometry("250x250")
def convert():
    a=infixex.get()
    ab=prefixfunction(a)
    l1=Label(root,text="the prefix conversion is {}".format(ab))
    l1.grid(row=2,column=1)

infix=StringVar()
infix_label=Label(root,text="Infix expression")
infix_label.grid(row=0,column=0)
infixex=Entry(root,textvariable=infix)
infixex.grid(row=0,column=1)
b1=Button(root,text="convert to prefix",command=convert)
b1.grid(row=1,column=1)

root.mainloop()
