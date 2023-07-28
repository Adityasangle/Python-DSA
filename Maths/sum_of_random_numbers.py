def sum(*args):
    sum=0
    for i in args[0]:
        sum = sum+i
    return sum


nums = list(map(int,input("enter numbers").split()))
print(sum(nums))