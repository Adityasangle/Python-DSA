def getwater(height):
    left = 0
    right = len(height)-1
    res=0
    leftMax = 0
    rightMax = 0
    while (left<=right):
        if height[left]<=height[right]:
            if height[left]>leftMax:
                leftMax = height[left]
            else:
                res+=leftMax-height[left]
            left+=1
        else:
            if height[right]>rightMax:
                rightMax = height[right]
            else:
                res+=rightMax-height[right]
            right+=1

    return res



def getwater2(arr,n):
    leftmax = [0]*len(arr)
    rightmax = [0]*len(arr)

    leftmax[0]=arr[0]
    for i in range(1,len(arr)):
        leftmax[i] = max(arr[i],leftmax[i-1])

    rightmax[len(arr)-1] = arr[len(arr)-1]
    for j in range(len(arr)-2,-1,-1):
        rightmax[j] = max(arr[j],rightmax[j+1])

    # print(leftmax, " ",rightmax)
    count = 0
    for i in range(n):
        count+=min(leftmax[i],rightmax[i])-arr[i]
    print(count)
height = [4,2,0,3,2,5]
print(getwater(height))
getwater2(height,6)
