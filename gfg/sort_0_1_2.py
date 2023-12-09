def sortZeroOneTwo(arr):
    l = 0
    m = 0
    h = len(arr) - 1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m] = arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m] == 1:
            m+=1
        else:
            arr[h],arr[m] = arr[m],arr[h]
            h-=1
    return arr

arr = sortZeroOneTwo([2,1,0,0,2,1,1])
print(arr)