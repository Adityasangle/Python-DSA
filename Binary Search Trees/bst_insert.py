class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




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
inorder(root)