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
    
    def extract_min(self):
        res = self.arr[0]
        n = len(self.arr)
        self.arr[0] = self.arr[n-1]
        self.arr.pop()
        self.min_heapify(0)
        return res
    
    def min_heapify(self,i): #top down
        lt = self.leftchild(i)
        rt = self.rightchild(i)
        smallest = i
        n = len(self.arr)
        if lt<n and self.arr[lt]<self.arr[smallest]:
            smallest = lt
        if rt<n  and self.arr[rt]<self.arr[smallest]:
            smallest = rt
        if smallest != i:
            self.arr[i],self.arr[smallest] = self.arr[smallest],self.arr[i]
            self.min_heapify(smallest)

    def delete(self,i):
        arr = self.arr
        n = len(arr)
        if i>n:
            return
        arr[i] = arr[n-1]
        arr.pop()
        self.min_heapify(i)




    def display(self):
        for i in self.arr:
            print(i,end = " ")
        

h = Heap()
h.insert(10)
h.insert(20)
h.insert(60)
h.insert(40)
h.insert(12)
h.display()
h.delete(1)
print()
h.display()
