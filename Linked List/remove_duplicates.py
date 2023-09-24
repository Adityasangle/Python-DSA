# checks if linked list is sorted ascending or descending
class Node:
    def __init__(self,k):
        self.data = k
        self.next = None


def remove_duplicates(head):
    if head == None:
        return None
    curr=head
    while curr.next!=None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def append(head,data):
    node = Node(data)
    if head == None:
        head = node
    else:
        curr=head
        while curr.next!=None:
            curr = curr.next
        curr.next = node
    return head

def display(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next


n = int(input("Enter number of nodes: "))
head = None
for i in range(n):
    data = int(input(f"Enter {i} element of node: "))
    if  i==0:
        head = append(head,data)
    else:
        head = append(head,data)

display(head)
print("/n")
head= remove_duplicates(head)
display(head)

    