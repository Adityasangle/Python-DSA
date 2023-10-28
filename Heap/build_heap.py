class Heap:
    def __init__(self):
        self.arr = []
    def parent(self,i):
        return int((i-1)//2)

    def leftchild(self,i):
        return 2*i+1
    
    def rightchild(self,i):
        return 2*i+2
    
    def build_heap(self,l):
        self.arr = l
        i = (len(l)-2)//2
        while i>=0:
            self.min_heapify(i)
            i=i-1

    def min_heapify(self,i):
        arr = self.arr
        lt = self.leftchild(i)
        rt = self.rightchild(i)
        n=len(self.arr)
        smallest = i
        if lt<n and arr[lt]<arr[smallest]:
            smallest = lt
        if rt<n and arr[rt]<arr[smallest]:
            smallest = rt
        if smallest!=i:
            arr[i],arr[smallest] = arr[smallest],arr[i]
            self.min_heapify(smallest)

    def display(self):
        for i in self.arr:
            print(i,end = " ")

        
l = [10,5,2,7,6,3,1]
h = Heap()
h.build_heap(l)
h.display()
