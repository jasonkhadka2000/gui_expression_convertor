def postfixtoinfix(input1):
    operators=["+","-","*","%","^","/"]
    outputstack=[]
    string1=[]
    stringer=""
    for i in input1:
        if i.isalpha():
            outputstack.append(i)
        if operators.count(i)==1:
            stringer=outputstack.pop()+i+outputstack.pop()
            outputstack.append(stringer)
            stringer=""
    output=outputstack[0][::-1]
    return "".join(output)
a="ab*"
print(postfixtoinfix(a))
