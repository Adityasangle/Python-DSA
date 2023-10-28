class Heap:
    def __init__(self):
        self.arr = []

    def parent(self,i):
        return int((i-1)//2)

    def leftchild(self,i):
        return 2*i+1
    
    def rightchild(self,i):
        return 2*i+2
    
    def insert(self,x):
        arr = self.arr
        arr.append(x)
        i = len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p = self.parent(i)
            arr[i],arr[p] = arr[p],arr[i]
            i = p
    
    def decrease(self,p,x):
        self.arr[p] = x
        while p!=0 and self.arr[p]<self.arr[self.parent(p)]:
            parent = self.parent(p)
            self.arr[p],self.arr[parent] = self.arr[parent],self.arr[p]
            p = parent


    def display(self):
        for i in self.arr:
            print(i,end = " ")
        

h = Heap()
h.insert(10)
h.insert(20)
h.insert(60)
h.insert(40)
h.display()
h.insert(12)
print()
h.display()
h.decrease(2,5)
print()
h.display()
        