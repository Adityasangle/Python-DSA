class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

def insert_in_place(head,data):
    node = Node(data)
    if head == None:
        head = node
    elif node.data<head.data:
        node.next = head
        head = node
    else:
        prev = None
        curr = head
        while curr!=None and node.data > curr.data:
            prev = curr
            curr = curr.next
        prev.next = node
        node.next = curr
    return head

def display(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next 

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

head = insert_in_place(head,45)
display(head)
        