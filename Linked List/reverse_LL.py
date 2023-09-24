class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

def reverse(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def display(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next
    print("\n")

head = reverse(head)
display(head=head)
