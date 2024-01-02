def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_double_sided_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        #print("combination: ",str_n[:i]," ",str_n[i:])
        if not is_prime(int(str_n[:i])) or not is_prime(int(str_n[i:])):
            return False
    return True

count = 0
num = 10
print("Double Sided Prime Numbers:")
while count < 11:
    if is_double_sided_prime(num):
        print(num)
        count += 1
    num += 1
