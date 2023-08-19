def uniques(arr):
    ans = 0
    for i in arr:
        ans = ans^i
    return ans

arr = [int(x) for x in input().split()]
print(uniques(arr))