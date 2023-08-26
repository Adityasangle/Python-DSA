def count_ones(arr,N):
    s=0
    e = len(arr)-1
    ans = -1
    while(s<=e):
        mid = s+(e-s)//2
        if arr[mid] == 1:
            ans = mid
            s = mid+1
        elif arr[mid]<1:
            e = mid-1
        else:
            s = mid+1
            
    return ans+1

arr = [int(x) for x in input("Enter array elements: ").split()]
print(count_ones(arr,len(arr)))