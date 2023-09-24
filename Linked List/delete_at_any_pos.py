class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

def deleteAtPosition(head, pos):
    #code here
    curr=head
    length = 1
    while curr.next!=None:
        length+=1
        curr=curr.next
    if pos == 1:
        temp=head.next
        head = temp
        return head
    else:
        curr=head
        for i in range(pos-2):
            curr=curr.next
        curr.next = curr.next.next if pos!=length else None
        return head


def display(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next 

head = deleteAtPosition(head,2)
display(head)
