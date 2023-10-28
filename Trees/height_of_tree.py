class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh,rh)+1

    
        

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)

print(height(root))
