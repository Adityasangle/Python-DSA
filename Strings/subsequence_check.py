def isSubSeq(s1, s2):
    i=j=0
    while (i<len(s1) and j<len(s2)):
        if s1[i] == s2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j == len(s2):
        return True
    else:
        return False

s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")
print(isSubSeq(s1,s2))
