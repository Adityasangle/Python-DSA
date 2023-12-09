def reorder(arr,index,n):
    i=0
    for i in range(n):
        while index[i]!=i:
            oldtargetI = index[index[i]]
            oldtargetE = arr[index[i]]

            arr[index[i]] = arr[i]
            index[index[i]] = index[i]

            arr[i] = oldtargetE
            index[i] = oldtargetI


arr = [50, 40, 70, 60, 90]
index= [3, 0, 4, 1, 2]
n = len(arr)
 
reorder(arr, index, n)
print(arr)
print(index)