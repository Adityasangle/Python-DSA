def union(a,b):
    res = [0 for _ in range(len(a)+len(b))]
    i = j = 0
    k = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            if k!=0 and a[i] == res[k-1]:
                i+=1
            else:
                res[k] = a[i]
                i+=1
                k+=1
        else:
            if k!=0 and b[j] == res[k-1]:
                j+=1
            else:
                res[k] = b[j]
                j+=1
                k+=1
    while i<len(a):
        if k!=0 and a[i] == res[k-1]:
                i+=1
        else:
            res[k] = a[i]
            i+=1
            k+=1 
    while j<len(b):
        if k!=0 and b[j] == res[k-1]:
                j+=1
        else:
            res[k] = b[j]
            j+=1
            k+=1

    print(res[:k])

a = [int(x) for x in input("Enter array elements for array 1: ").split()]
b = [int(x) for x in input("Enter array elements for array 2: ").split()]

union(a,b)