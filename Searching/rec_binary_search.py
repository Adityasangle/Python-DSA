def search(arr,key,s,e):
    if s>e:
        return -1
    mid = (s+e)//2
    if arr[mid] == key:
        return mid
    elif arr[mid]>key:
        return search(arr,key,s,mid-1)
    else:
        return search(arr,key,mid+1,e)

arr = [int(x) for x in input("Enter array elemenets: ").split()]
key = int(input("Enter key: "))
print(search(arr,key,0,len(arr)-1))