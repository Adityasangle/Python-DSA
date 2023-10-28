#No of nodes in tree
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def size(root):
    if root is None:
        return 0
    else:
        count = 0
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            count+=1

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return count
    

def sizeRecursive(root):
    if root is None:
        return 0
    else:
        ls = sizeRecursive(root.left)
        rs = sizeRecursive(root.right)
        return ls+rs+1


    
        

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)

print(sizeRecursive(root))
