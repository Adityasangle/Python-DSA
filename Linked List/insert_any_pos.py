class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

def insert(head,data,pos):
    node = Node(data)
    if pos == 1:
        node.next = head
        head = node
        return head
    curr = head
    for i in range(pos-2):
        if curr.next!=None:
            curr = curr.next
        else:
            return head
    node.next = curr.next
    curr.next =node
    return head
    
def display(head):
    curr = head
    while curr!= None:
        print(curr.data,end = " ")
        curr = curr.next

head = insert(head,45,5)
display(head)