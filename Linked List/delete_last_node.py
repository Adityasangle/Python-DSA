def delete_last_node(head):
    if head == None:
        return None
    elif head.next==None:
        return None
    curr = head
    while curr.next.next !=None:
        curr = curr.next
    curr.next = None
    return head

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

def display(head):
    curr = head
    while curr!= None:
        print(curr.data,end = " ")
        curr = curr.next

head = delete_last_node(head)
display(head)