#Given an Unsorted array of integers, find 2 elements which occur odd number of times
def OddOccurences(l):
    res = 0
    x = 0
    y=0
    for i in l:
        res = res^i

    set_bit_no = res & (~(res-1))

    for i in l:
        if i & set_bit_no:
            x = x^i
        else:
            y = y^i
    return x,y

x,y = OddOccurences([2,3,9,3,5,5,1,3,2,1])
print(x,y)
