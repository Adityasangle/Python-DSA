def count_bits(n):
    count = 0
    while n:
        n = n&(n-1)
        count+=1
    return count


print(count_bits(14))