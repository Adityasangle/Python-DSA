class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

def middle_of_ll(head):
    if head == None:
        return None
    prev = head
    curr=head
    while curr!=None and curr.next!=None:
        prev = prev.next
        curr = curr.next.next
    return prev.data


def display(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next 

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


n = int(input("Enter number of nodes: "))
head = None
for i in range(n):
    data = int(input(f"Enter {i} element of node: "))
    if  i==0:
        head = append(head,data)
    else:
        head = append(head,data)

display(head)
middle_node_data = middle_of_ll(head)
print("middle node is : ",middle_node_data)        