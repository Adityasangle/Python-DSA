# checks if linked list is sorted ascending or descending
class Node:
    def __init__(self,k):
        self.data = k
        self.next = None


def is_Sorted(head):
    if not head:
        return 1
    
    cur = head
    
    total_length = 0
    asc_length = 0
    desc_length = 0
    while cur.next:
        if cur.data <= cur.next.data:
            asc_length += 1
        if cur.data >= cur.next.data:
            desc_length += 1
        total_length += 1
        cur = cur.next
    
    return int((asc_length == total_length) or (desc_length == total_length))

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
if is_Sorted(head):
    print("Sorted")
else:
    print("Not Sorted")
    