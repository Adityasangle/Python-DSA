def squares(n):
    i=1
    while(i<=n):
        yield i*i
        i+=1

for i in squares(25):
    print(i)

print("**************************************")
def prime_nums(n):
    x = 2
    while(x<n):
        flag = 0
        for i in range(2,x):
            if x%i==0:
                flag = 1
                x+=1
        if flag==0:
            yield x
            x+=1

for i in prime_nums(50):
    print(i)