class Stack:
    def __init__(self):
        self.stack = [-1]*1000
        self.top = -1
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False    
    
    def push(self,x):
        self.top+=1
        self.stack[self.top] = x
    def pop(self):
        self.stack[self.top] = -1
        self.top-=1
    def peek(self):
        return self.stack[self.top]
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())
