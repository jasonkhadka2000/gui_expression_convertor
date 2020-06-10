def prefixtoinfix(input1):
    input1=input1[::-1]
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
    return "".join(outputstack)




