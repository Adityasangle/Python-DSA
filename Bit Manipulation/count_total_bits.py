

def count_total_bits(n):
    res = [0]*(n+1)
    for i in range(1,n+1):
        res[i] = res[i//2]+i%2
    return sum(res)

print(count_total_bits(5))
print([x if x % 2 == 0 else x * 2 for x in range(10)])