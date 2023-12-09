from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        loc = {}
        res = []
        for idx, ele in enumerate(nums2):
            loc[ele] = idx

        for i in nums1:
            flag = 0
            pos = loc[i]
            print(pos)
            if pos == len(nums2)-1:
                res.append(-1)
            else:
                for j in range(pos+1,len(nums2)):
                    if nums2[j]>i:
                        res.append(nums2[j])
                        flag=1
                        break
                if flag==0:
                    res.append(-1)
        return res
        
res = nextGreaterElement([4,1,2],[1,3,4,2])
print(res)