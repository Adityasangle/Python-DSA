class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
    def display(self):
        curr = self.head
        while curr!=None:
            print(curr.data,end = " ")
            curr =curr.next

        print("\n")
    def insert_at_beg(self):
        data = int(input("Enter data for node: "))
        node = Node(data)
        node.next = self.head
        self.head = node
        
print("Linked List Basics")

number_of_nodes = int(input("Enter Number of Nodes \n"))
ll=LinkedList()
for i in range(number_of_nodes):
    node_data = int(input(f"ENter data for {i} node \n"))
    node = Node(node_data)
    ll.append(node)
ll.display()
ll.insert_at_beg()
ll.display()