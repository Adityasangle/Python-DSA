def removePair(s):
        # code here
        st = []
        for i in s[::-1]:
            if st == []:
               st.append(i)
            else:
                if i == st[-1]:
                    st.pop()
                else:
                    st.append(i)
        
        res = ""
        while st:
            res+=st[-1]
            st.pop()
        return res

s = input("ENter string: ")
print(removePair(s))