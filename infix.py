##infix to post expresion
def infixtopostfix(input1):
    priority={'+':0,'-':0,'*':1,'%':1,'^':3,'/':2}
    operators=[keys for keys in priority.keys()]
    opening_paranthesis=["[","{","("]
    closing_paranthesis=["]","}",")"]
    outputstack=[]
    tempstack=[]
    #print("output stack","tempstack",sep="\t")
    for i in input1:
        if i.isalpha():
            outputstack.append(i)
            print("".join(outputstack),"".join(tempstack),sep="\t")
        elif opening_paranthesis.count(i)==1:
            tempstack.append(i)
            print("".join(outputstack), "".join(tempstack), sep="\t")
        elif operators.count(i)==1:
            if len(tempstack)==0:
                tempstack.append(i)
            elif opening_paranthesis.count(tempstack[-1])==1:
                tempstack.append(i)
            elif priority.get(i)>=priority.get(tempstack[-1]):
                tempstack.append(i)
            else:
                x=tempstack.pop()
                outputstack.append(x)
                tempstack.append(i)
            print("".join(outputstack), "".join(tempstack), sep="\t")
        elif closing_paranthesis.count(i)==1:
            while opening_paranthesis.count(tempstack[-1])!=1:
                x=tempstack.pop()
                outputstack.append(x)
            unwanted=tempstack.pop()
            print("".join(outputstack), "".join(tempstack), sep="\t")
        else:
            return "input error"
    while len(tempstack)!=0:
        a=tempstack.pop()
        if opening_paranthesis.count(a)!=1:
            outputstack.append(a)
    print("".join(outputstack), "".join(tempstack), sep="\t")
    return "".join(outputstack)

#infix to prefix expression
def infixtoprefix(input1):
    input1=input1[::-1]
    priority={'+':0,'-':0,'*':1,'%':1,'^':3,'/':2}
    operators=[keys for keys in priority.keys()]
    closing_paranthesis=["[","{","("]
    opening_paranthesis=["]","}",")"]
    outputstack=[]
    tempstack=[]
    print("hello world")
    #print("output stack","tempstack",sep="\t")
    for i in input1:
        if i.isalpha():
            outputstack.append(i)
            #print("".join(outputstack),"".join(tempstack),sep="\t")
        elif opening_paranthesis.count(i)==1:
            tempstack.append(i)
            #print("".join(outputstack), "".join(tempstack), sep="\t")
        elif operators.count(i)==1:
            if len(tempstack)==0:
                tempstack.append(i)
            elif opening_paranthesis.count(tempstack[-1])==1:
                tempstack.append(i)
            elif priority.get(i)>=priority.get(tempstack[-1]):
                tempstack.append(i)
            else:
                x=tempstack.pop()
                outputstack.append(x)
                tempstack.append(i)
            #print("".join(outputstack), "".join(tempstack), sep="\t")
        elif closing_paranthesis.count(i)==1:
            while opening_paranthesis.count(tempstack[-1])!=1:
                x=tempstack.pop()
                outputstack.append(x)
            unwanted=tempstack.pop()
            #print("".join(outputstack), "".join(tempstack), sep="\t")
        else:
            return "input error"
    while len(tempstack)!=0:
        a=tempstack.pop()
        if opening_paranthesis.count(a)!=1:
            outputstack.append(a)
    #print("".join(outputstack), "".join(tempstack), sep="\t")
    return "".join(outputstack[::-1])

def main():
    input1=input("Enter prefix expression: hai ")
    print(f"the required expression is {infixtopostfix(input1)}")
if __name__ == '__main__':
    main()






