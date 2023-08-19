def left_rotate_by_one(arr,n):
    arr = arr[1:n]+[arr[0]]
    return arr
arr= [int(x) for x in input().split()]
print(left_rotate_by_one(arr,len(arr)))

def left_rotate_by_num(arr,n,d):
    d = d%n
    