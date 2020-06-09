from tkinter import *
from infix import *
from postfix import *
from prefix import *

def Evaluate():
    inputtype=choicevar.get()
    outputtype=choicevar1.get()
    input1=list(input_expression.get())
    if inputtype==outputtype:
        outputexpression=input1
    else:
        if inputtype=="infix":
            if outputtype=="postfix":
                outputexpression=infixtopostfix(input1)
            else:
                outputexpression=infixtoprefix(input1)
        elif inputtype=="prefix":
            if outputtype=="postfix":
                intermediate=prefixtoinfix(input1)
                outputexpression=infixtopostfix(intermediate)
            else:
                outputexpression=prefixtoinfix(input1)
        else:
            if outputtype=="prefix":
                intermediate=postfixtoinfix(input1)
                outputexpression=infixtoprefix(intermediate)
            else:
                outputexpression=postfixtoinfix(input1)
    output1 = Label(root, text="The required expression is:", font="timesnewroman 12 bold", pady=5).grid(row=6, column=0)
    output = Label(root, text=outputexpression, font="timesnewroman 12", pady=5,relief="sunken").grid(row=6,column=1)

    print(outputexpression)

root=Tk()
root.geometry("700x300")
root.maxsize(width=700,height=300)
root.minsize(width=700,height=300)
root.title("Expression converter by mrjk")
root.iconbitmap("icon/mrjk.ico")


title="\t"*4
title_label=Label(root,text=title).grid(row=0,column=0)
title="Input Expession"
title_label=Label(root,text=title,font="timesnewroman 12 bold").grid(row=0,column=1,pady=8)

choicevar=StringVar()
choicevar.set("anything")
radio=Radiobutton(root,text="Infix",variable=choicevar,value="infix").grid(row=1,column=0)
radio1=Radiobutton(root,text="Prefix",variable=choicevar,value="prefix").grid(row=1,column=1)
radio2=Radiobutton(root,text="Postfix",variable=choicevar,padx=25,value="postfix").grid(row=1,column=2)


l1=Label(root,text="Enter expression:",font="timesnewroman 10 bold")
l1.grid(row=2,column=0)
input_expression=StringVar()
a=Entry(root,textvariable=input_expression).grid(row=2,column=1,padx=8)


#canvas=Canvas(root,width=600,height=600)
#canvas.grid()
# canvas.create_line(100,100,200,200)
l=Label(root,text="-"*50).grid(row=3,column=1,pady=30)

title="\t"*4
title_label=Label(root,text=title).grid(row=4,column=1)
title="Conversion Expression"
title_label=Label(root,text=title,font="timesnewroman 12 bold").grid(row=4,column=1,pady=8)

choicevar1=StringVar()
choicevar1.set("anything")
radio=Radiobutton(root,text="Infix",variable=choicevar1,value="infix").grid(row=5,column=0)
radio=Radiobutton(root,text="Prefix",variable=choicevar1,value="prefix").grid(row=5,column=1)
radio=Radiobutton(root,text="Postfix",variable=choicevar1,padx=25,value="postfix").grid(row=5,column=2)
convert_button=Button(root,text="convert",command=Evaluate).grid(row=5,column=4)



root.mainloop()
