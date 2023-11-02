def maxConsecutiveOnes(n):
    count = 0
    maxCount = 0
    while n:
        if n&1:
            count+=1
            maxCount = max(count,maxCount)
        else:
            count = 0
        n =n>>1
    return count

print(maxConsecutiveOnes(15))