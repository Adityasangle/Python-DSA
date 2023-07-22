def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

ans = linear_search([1,2,3,4,5],5)
print(ans)