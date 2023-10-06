def postToInfix(postfix):
        # Code here
        st = []
        for i in postfix:
            if i.isalpha() or i.isdigit():
                st.append(i)
            else:
                op1 = st[-1]
                st.pop()
                op2 = st[-1]
                st.pop()
                st.append("("+op2+i+op1+")")
        return st[0]

exp = input("Enter postfix expression:")
postfix = postToInfix(exp)
print(postfix)