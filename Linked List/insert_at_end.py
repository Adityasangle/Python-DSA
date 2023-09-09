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

def insert_at_end(head):
    data = int(input("Enter data for node: "))
    node = Node(data)
    if head == None:
        return node
    curr = head
    while curr.next !=None:
        curr = curr.next
    curr.next =node
    return head
    
def display(head):
    curr = head
    while curr!= None:
        print(curr.data,end = " ")
        curr = curr.next

head = insert_at_end(head)
display(head)