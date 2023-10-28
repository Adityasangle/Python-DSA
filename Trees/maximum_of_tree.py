#No of nodes in tree
from collections import deque
import math
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    

def maximum(root):
    if root is None:
        return -math.inf
    else:
        lmax = maximum(root.left)
        rmax = maximum(root.right)
        return max(root.data,lmax,rmax)


    
        

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)

print(maximum(root))
