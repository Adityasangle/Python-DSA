def find_peak(arr):
    s = 0
    e = len(arr)-1
    while(s<e):
        mid = s+(e-s)//2
        if arr[mid]<arr[mid+1]:
            s = mid+1
        else:
            e = mid
    return s


arr = [int(x) for x in input("Enter array elements: ").split()]
print(find_peak(arr))