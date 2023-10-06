class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = node
            node.prev=curr
            self.tail = node

    def display(self):
        curr =self.head
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next
        print("\n")

    def inserAtBeg(self,data):
        node  = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def insertAtpos(self,pos,data):
        node = Node(data)
        if pos == 0:
            node.next = self.head.next
            if self.head.next is not None:
                node.next.prev=node
            self.head.next = node
            node.prev = self.head
        else:
            curr = self.head
            for i in range(pos):
                if curr is None:
                    return 
                curr = curr.next
            node.next = curr.next
            if curr.next is not None:
                curr.next.prev = node
            curr.next = node
            node.prev = curr

print("Linked List Basics")

number_of_nodes = int(input("Enter Number of Nodes \n"))
ll=LinkedList()
for i in range(number_of_nodes):
    node_data = int(input(f"ENter data for {i} node \n"))
    ll.append(node_data)
ll.display()
ll.inserAtBeg(5)
ll.display()
ll.insertAtpos(2,69)
ll.display()
        