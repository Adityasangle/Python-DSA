
def solve(arr,ans,index):
    if index>len(arr)-1:
        ans.append(arr[:])
        return 
    for j in range(index,len(arr)):
        arr[index],arr[j]=arr[j],arr[index]
        solve(arr,ans,index+1)
        arr[index],arr[j]=arr[j],arr[index]

def permutaions(arr):
    index = 0
    ans = []
    solve(arr,ans,index)
    return ans

arr = permutaions([1,2,3])
print(arr)
                  