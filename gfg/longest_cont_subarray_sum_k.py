def longContSubArraySumK(arr,k):
    sum = 0
    maxlen = 0
    presum = {}
    for i in range(len(arr)):
        sum+=arr[i]
        if sum == k:
            maxlen = max(maxlen,i+1)
        diff = sum-k
        if diff in presum:
            maxlen = max(maxlen,i-presum[diff])
        else:
            presum[sum]=i
    return maxlen

maxlen = longContSubArraySumK([1,5,2,6,7,-2,3],5)
print(maxlen)