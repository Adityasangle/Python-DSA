def powerSet(s):
    n = len(s)
    psize = 1<<n
    for i in range(psize):
        for j in range(n):
            if i&(1<<j):
                print(s[j],end = " ")
        print()

print(powerSet("abc"))