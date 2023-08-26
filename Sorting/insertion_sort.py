def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        j = i-1
        x = arr[i]
        while j>=0 and arr[j]>x:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x
    return arr


arr = [int(x) for x in input("Enter array elements: ").split()]
print(insertion_sort(arr))