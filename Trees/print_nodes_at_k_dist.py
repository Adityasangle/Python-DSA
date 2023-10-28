class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def printkdist(root,k):
    if root is None:
        return
    elif k == 0:
        print(root.data,end = " ")
    else:
        printkdist(root.left,k-1)
        printkdist(root.right,k-1)

    
        

root = Node(10)
root.left = Node(20) 
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)

print(printkdist(root,3))
