def countBitsFlip(a,b):
        ##Your code here
        count = 0
        if a==b:
            return 0
        while a and b:
            if a&1 != b&1:
                count+=1
            a = a>>1
            b= b>>1
        while a:
            a = a&(a-1)
            count+=1
        while b:
            b = b&(b-1)
            count+=1
        return count


#method2
def countBitsFlip2(a,b):
    count = 0
    x = a^b
    while x:
        x = x & (x-1)
        count+=1
    return count
    



print(countBitsFlip2(78,4))