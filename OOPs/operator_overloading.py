class number():
    def __init__(self,x):
        self.num = x

    def __add__(self,y):
        return self.num+y.num

    

num1 = number(3)
num2 = number(4)

num = num1+num2
print(num)


