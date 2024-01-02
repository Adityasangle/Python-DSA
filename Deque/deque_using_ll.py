class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0
    
    def insertFront(self,x):
        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
            self.sz+=1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.sz+=1

    def insertRear(self,x):
        node = Node(x)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.sz+=1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.sz+=1

    def deleteRear(self):
        if self.tail is None:
            print("Deque is Empty")
        elif self.sz == 1:
            print(f"Deleted {self.tail.data} from Deque")
            self.head  = None
            self.tail = None
            self.sz-=1
        else:
            print(f"Deleted {self.tail.data} from Rear")
            temp = self.tail.prev
            self.tail.prev = None
            self.tail = temp
            temp.next = None
            self.sz-=1

    def deleteFront(self):
        if self.head == None:
            print("Deque is Empty")
        elif self.head.next == None:
            self.head = None
            self.tail = None
            self.sz-=1
        else:
            temp = self.head.next
            print(f"Deleted {self.head.data} from front")
            self.head.next = None
            temp.prev = None
            self.head = temp
            self.sz-=1
    
    def getSize(self):
        print(f"Size of Deque is: {self.sz}")

    def isEmpty(self):
        return self.sz==0
    
    def display(self):
        if self.head is None:
            print("Deque is Empty")
        else:
            curr = self.head
            while curr:
                print(curr.data,end = " ")
                curr = curr.next
            


d = Deque()
d.insertFront(10)
d.insertFront(20)
d.insertRear(30)
d.display()
d.deleteFront()
d.display()

        