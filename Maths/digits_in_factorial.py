import math

def digitsInFactorial(N):
        # code here
        res=0
        for i in range(2,N+1):
            res+=math.log10(i)
        return math.floor(res+1)


print(digitsInFactorial(5))