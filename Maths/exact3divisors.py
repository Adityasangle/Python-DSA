def exact3divisors(N):
    count=0
    i=2
    while(i*i<=N):
        if(isPrime(i) and i*i<=N):
            count+=1
        i+=1
    return count

def isPrime(n):
    if n==1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        i=5
        while(i*i<=n):
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True

print(exact3divisors(10))