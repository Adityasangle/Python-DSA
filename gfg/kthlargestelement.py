import heapq

def kthlargest(arr,k):
    
    h = []
    for i in range(len(arr)):
        heapq.heappush(h,-arr[i])

    for i in range(k-1):
        heapq.heappop(h)
    
    ans = heapq.heappop(h)
    return -ans


print(kthlargest([6,1,8,3,9],1))
