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

height = [4,2,0,3,2,5]
print(getwater(height))
