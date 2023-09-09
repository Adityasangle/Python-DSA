from collections import defaultdict
import sys
def leftmost_repeating_char(s1):
    chars = defaultdict(lambda: 0)
    for i in s1:
        chars[i]+=1
    for i in range(len(s1)):
        if chars[s1[i]]>1:
            return i
    return -1


def efficient_leftmost_repeating_char(s1):
    res= sys.maxsize
    chars = [-1] *256
    for i in range(len(s1)):
        if chars[ord(s1[i])] == -1:
            chars[ord(s1[i])] = i
        else:
            res = min(res,chars[ord(s1[i])])
    if res == sys.maxsize:
        return -1
    return res



s1 = input("Enter string s1: ")
print(efficient_leftmost_repeating_char(s1))