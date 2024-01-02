def powerset(arr,n):
    psize = 1<<n
    res = []
    for i in range(psize):
        temp = []
        for j in range(n):
            if i&(1<<j):
                temp.append(arr[j])
        res.append(temp)

    return res

res = powerset([1,2,3],3)
print(res)