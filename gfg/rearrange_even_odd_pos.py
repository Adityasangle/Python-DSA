# Given an array A of n elements, rearrange the array according to the following relations :
# A[i] >= A[i-1], if i is even.
# A[i] <= A[i-1], if i is odd.[Considering 1-indexed array]
# Return the resultant array.

def assign (arr,  n) : 
        #Complete the function
        for i in range(1,n):
            if (i+1)%2==0:
                if arr[i]<arr[i-1]:
                    arr[i-1],arr[i] = arr[i],arr[i-1]
            else:
                if arr[i]>arr[i-1]:
                    arr[i-1],arr[i] = arr[i],arr[i-1]
        return arr

def assign2(arr,  n) : 
        #Complete the function
        arr.sort()
        res=[0]*n
        p=0
        q = len(arr)-1
        for i in range(n):
            if (i+1)%2 == 0:
                res[i] = arr[q]
                q=q-1
            else:
                res[i] = arr[p]
                p+=1
        return res
arr = assign2([2,5,3,1,9,6],6)
print(arr)