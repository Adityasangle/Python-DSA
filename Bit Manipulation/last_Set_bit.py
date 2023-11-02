def lastSetBit(n):
    res=1
    while n:
        if n&1:
            return res
        n = n>>1
        res+=1

print(lastSetBit(16)) #10000