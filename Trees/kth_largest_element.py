import heapq

def kth_largest_element(arr,k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    print(f"After heapifying initial {min_heap}",end="\n")
    for num in arr[k:]:
        print(f"Heap: {min_heap} ",end = "\n")
        if num>min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap,num)

    return min_heap[0]

kth_largest_element( [3, 1, 8, 4, 7, 5, 6, 2],3)

