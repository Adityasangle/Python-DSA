def infix_to_postfix(exp):
    postfix = ""
    stack = []
    exp_list = ["+","-","*","/","^"]
    for i in exp:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1]!="(":
                postfix+=stack.pop()
            stack.pop()
        elif i in exp_list:
            while stack and priority(stack[-1])>=priority(i):
                postfix+=stack.pop()
            stack.append(i)
        else:
            postfix+=i
        
    while len(stack)>0:
        postfix+=stack.pop()
    return postfix


def priority(ch):
    if ch == "(":
        return 0
    elif ch == "+" or ch=="-":
        return 1
    elif ch == "*" or ch=="/":
        return 2
    else:
        return 3
    

exp = input("Enter infix expression:")
postfix = infix_to_postfix(exp)
print(postfix)

