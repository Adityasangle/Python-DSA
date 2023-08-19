#Sieve of Eratosthenes is a method for finding all primes up to 
# (and possibly including) a given natural. 
# This method works well when is relatively small, 
# allowing us to determine whether any natural number less than or equal to is prime or composite.

def sieve_of_era(n):
    if n<=1:
        return
    isPrime = [True for i in range(n+1)]
    i=2
    primes = []
    while(i<=n):
        if isPrime[i]:
            primes.append(i)
            for j in range(i*i,n+1,i):
                isPrime[j] = False
        i+=1
    return primes

print(sieve_of_era(10))
