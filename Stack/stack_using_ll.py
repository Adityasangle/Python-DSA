class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.sz = 0

    def isEmpty(self):
        return True if self.sz==0 else False
    
    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        print(f"Added {x} to the Stack\n")
        self.sz+=1

    def pop(self):
        if self.sz ==0:
            raise "Stack already empty\n"
        else:
            self.sz-=1
            del_data = self.head.data
            print(f"Popped {del_data} from Stack\n")
            self.head = self.head.next

    def peek(self):
        if self.sz!=0:
            print(self.head.data,end = "\n")
        else:
            raise "Stack Already Empty\n"


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.peek()
stack.pop()
stack.pop()
stack.peek()
stack.pop()
stack.pop()



    

