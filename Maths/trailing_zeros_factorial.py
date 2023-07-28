def trailing_zeros_fact(N):
    count = 0
    for i in range(5,N+1,5):
        if i%5==0:
            num=i
            while(num%5==0):
                num=num//5
                count+=1
    return count

print(trailing_zeros_fact(25))