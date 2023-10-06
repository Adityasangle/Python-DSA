def isOperand(ch):
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9'):
        return True
    else:
        return False
    

def prefix_to_infix(exp):
    stack = []
    for i in range(len(exp)-1,-1,-1):
        if isOperand(exp[i]):
            stack.append(exp[i])
        else:
            a=stack[-1]
            stack.pop()
            b=stack[-1]
            stack.pop()
            stack.append(f"({a}{exp[i]}{b})")
    return stack[0]


exp = input("Enter infix expression:")
prefix = prefix_to_infix(exp)
print(prefix)