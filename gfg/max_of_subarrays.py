from collections import deque
def max_of_subarrays(arr,n,k):
        res = []
        d = deque()
        for i in range(n):
            while d and d[0]<i-k+1:
                d.popleft()
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
                
            d.append(i)
            
            if i>=k-1:
                res.append(arr[d[0]])
        return res

res = max_of_subarrays([1,2,3,1,4,5,2,3],8,3)
print(res)