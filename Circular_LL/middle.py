class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = head


def find_middle(head):
    if head.next == head:
            return head.data
    first = head
    second =  head
    while second.next!=head and second.next.next!= head:
        second = second.next.next
        first = first.next
    return first.data
middle = find_middle(head)
print(middle)