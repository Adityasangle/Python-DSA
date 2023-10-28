class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def isEmpty(self):
        return self.sz==0
    
    def enqueue(self,x):
        node = Node(x)
        if self.rear == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.sz+=1

    def deque(self):
        if self.front == None:
            print("Queue is Empty")
        elif self.front.next == None:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.sz-=1

    def display(self):
        curr = self.front
        while curr:
            print(curr.data,end = " ")
            curr = curr.next
        print()
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.deque()
q.deque()
q.deque()
q.display()
q.deque()
