from collections import deque



class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.data = k


def display_rightview(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        n = len(q)

        while n>0:
            n-=1
            node = q.popleft()

            if n==0:
                print(node.data,end = " ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)

display_rightview(root)