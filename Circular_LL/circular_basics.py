class Node:
    def __init__(self,k):
        self.data = k
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail=node
            node.next = self.head

    def display(self):
        curr = self.head
        print(curr.data,end = " ")
        curr = curr.next
        while curr!=self.head:
            print(curr.data,end = " ")
            curr = curr.next

        print("\n")

        
    def insert_at_beg(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node






number_of_nodes = int(input("Enter Number of Nodes \n"))
ll=CircularLinkedList()
for i in range(number_of_nodes):
    node_data = int(input(f"ENter data for {i} node \n"))
    node = Node(node_data)
    ll.append(node)
ll.display()
ll.insert_at_beg(50)
ll.display()