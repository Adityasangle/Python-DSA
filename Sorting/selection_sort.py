def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if arr[k]>arr[j]:
                k=j
        arr[i],arr[k]=arr[k],arr[i]
    return arr


arr = [int(x) for x in input("Enter array elements: ").split()]
print(selection_sort(arr))