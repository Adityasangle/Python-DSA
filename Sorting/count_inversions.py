def count_inv(arr,l,r):
    res=0
    if(r>l):
        mid = l+(r-l)//2
        res+=count_inv(arr,l,mid)
        res+=count_inv(arr,mid+1,r)
        res+=count_merge(arr,l,mid,r)

    return res

def count_merge(arr,l,m,r):
    left  = arr[l:m+1]
    right = arr[m+1:r+1]
    i=j=0
    k=l
    res = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
            res+=len(left)-i
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return res

a = [int(x) for x in input("Enter array elements for array: ").split()]


print(count_inv(a,0,len(a)))