def merge(arr,l,m,r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i=j=0
    k=l
    while i <len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1

def merge_sort(arr,l,r):
    if r>l:
        m = l+(r-l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
    

arr = [int(x) for x in input("Enter array elements: ").split()]
merge_sort(arr,0,len(arr)-1)
print(*arr)