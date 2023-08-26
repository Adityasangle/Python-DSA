def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

arr = [int(x) for x in input("Enter array elements: ").split()]
print(bubble_sort(arr))