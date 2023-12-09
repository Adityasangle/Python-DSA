
def equilibrium(arr):
    total_sum = 0
    for i in arr:
        total_sum+=i
    left_sum = 0
    for i in range(len(arr)):
        total_sum-=arr[i]
        if left_sum == total_sum:
            return i
        left_sum+=arr[i]
    
    return -1

idx = equilibrium([1,3,5,2,2])
print(idx)