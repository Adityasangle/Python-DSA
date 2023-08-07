def prime_factorization(n):
    prime_factors = []
    i=2
    while(n//i!=0):
        if (is_prime_number(i)):
            while(n%i==0):
                n=n//i
                prime_factors.append(i)
        i+=1
    return prime_factors



def is_prime_number(n):
    if n==1:
        return False
    if n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True


print(prime_factorization(315))