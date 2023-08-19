def last_occurence(arr,k):
    s = 0
    e = len(arr)-1
    ans = -1
    while(s<=e):
        mid = s+(e-s)//2
        if arr[mid] == k:
            ans = mid
            s = mid+1
        elif arr[mid]>k:
            e = mid-1
        else:
            s = mid+1
    return ans

arr = [int(x) for x in input("Enter elements: ").split()]
k = int(input("Enter key: "))
print(last_occurence(arr,k))