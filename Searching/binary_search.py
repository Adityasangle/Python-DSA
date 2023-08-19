def search(arr,key):
    s=0
    e=len(arr)-1
    
    while(s<=e):
        mid = (s+e)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] >key:
            e = mid-1
        else:
            s = mid+1
    return -1
arr = [int(x) for x in input("Enter array elemenets: ").split()]
key = int(input("Enter key: "))
print(search(arr,key))