class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = head

def del_node_at_first(head):
    if head is None:
        return None
    if head.next == head:
        return None
    
    head.data = head.next.data
    head.next = head.next.next

    return head


def display(head):
    curr = head
    print(curr.data,end = " ")
    curr = curr.next
    while curr!=head:
        print(curr.data,end = " ")
        curr =curr.next

head = del_node_at_first(head)
display(head)
