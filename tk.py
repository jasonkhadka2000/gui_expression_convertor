from tkinter import *
from infix import *
functiontype=""
def inputexpressionchoice():
    pass

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
expression_choice=Button(root,text="choose",command="inputexpressionchoice").grid(row=1,column=4)

l1=Label(root,text="Enter expression:",font="timesnewroman 10 bold")
l1.grid(row=2,column=0)
input_expression=StringVar()
a=Entry(root,textvariable=input_expression).grid(row=2,column=1,padx=8)
Enter=Button(root,text="Enter",command="convert").grid(row=2,column=2)

#canvas=Canvas(root,width=600,height=600)
#canvas.grid()
# canvas.create_line(100,100,200,200)
l=Label(root,text="-"*50).grid(row=3,column=1,pady=30)

title="\t"*4
title_label=Label(root,text=title).grid(row=4,column=1)
title="Conversion Expression"
title_label=Label(root,text=title,font="timesnewroman 12 bold").grid(row=4,column=1,pady=8)

choicevar=StringVar()
choicevar.set("anything")
radio=Radiobutton(root,text="Infix",variable=choicevar,value="infix").grid(row=5,column=0)
radio=Radiobutton(root,text="Prefix",variable=choicevar,value="prefix").grid(row=5,column=1)
radio=Radiobutton(root,text="Postfix",variable=choicevar,padx=25,value="postfix").grid(row=5,column=2)
convert_button=Button(root,text="convert",command="choose").grid(row=5,column=4)

output=Label(root,text="The output is:  ....to fill....",font="timesnewroman 12 bold",pady=5).grid(row=6,column=0)

root.mainloop()
