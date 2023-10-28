class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def getsucc(curr):
    while curr.left:
        curr = curr.left
    return curr.data

def delete(root,x):
    if root is None:
        return
    elif root.data>x:
        root.left = delete(root.left,x)
    elif root.data<x:
        root.right = delete(root.right,x)
    else: #same value found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = getsucc(root.right)
            root.data = succ
            root.right = delete(root.right,succ)
    return root

def insert(root,x):
    if root is None:
        return Node(x)
    elif root.data ==x:
        return
    elif root.data>x:
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)
    return root    


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

root = None
root = insert(root,10)
root = insert(root,20)
root = insert(root,6)
root = insert(root,9)
root = insert(root,3)
root = insert(root,30)

inorder(root)
root = delete(root,6)
print()
inorder(root)
