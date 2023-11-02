def max_and(arr):
    res = 0
    for bit in range(31,-1,-1):
        count = 0
        pattern = res|(1<<bit)
        for item in arr:
            if item&pattern ==pattern:
                count+=1
        if count>=2:
            res = pattern
    
    return res

print(max_and([1,2,3,4,5]))