def findFloor(A,N,X):
        #Your code here
        s = 0
        e = N-1
        ans = -1
        while(s<=e):
            mid = s+(e-s)//2
            if A[mid] == X:
                ans = mid
                s = mid+1
            elif A[mid]>X:
                e = mid-1
            else:
                ans = mid
                s = mid+1
        return ans

arr = [int(x) for x in input("Enter array elements: ").split()]
print(findFloor(arr,len(arr),112))