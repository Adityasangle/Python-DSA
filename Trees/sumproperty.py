from collections import deque

# Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def sumprop(root):
    if not root:
            return 1
    else:
        q = deque()
        q.append(root)
        while len(q)>0:
            curr = q.popleft()
            if curr.left is None and curr.right is None:
                return 1
            data1 = data2 = 0
            if curr.left:
                data1 = curr.left.data
                q.append(curr.left)
            if curr.right:
                data2 = curr.right.data
                q.append(curr.right)
            if curr.data!=data1+data2:
                return 0
        return 1
    
root = Node(10)
root.left = Node(10)
print(sumprop(root))