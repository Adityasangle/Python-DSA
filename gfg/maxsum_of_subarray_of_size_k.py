def subarray_maxsum(arr,k):
    maxsum = sum(arr[:k])
    curr_sum = maxsum
    for i in range(k,len(arr)):
        curr_sum = curr_sum+arr[i]-arr[i-k]
        maxsum = max(curr_sum,maxsum)
    return maxsum

maxsum = subarray_maxsum([1,6,2,5,8,3,2,-2,8],3)
print(maxsum)
