class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def search(root,x):
    if root is None:
        return False
    if root.data == x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.right,x)
    
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


root = None
root = insert(root,10)
root = insert(root,20)
root = insert(root,6)
root = insert(root,9)
root = insert(root,3)
print(search(root,14))