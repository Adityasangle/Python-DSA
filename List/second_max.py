def second_largest(l):
    max = l[0]
    smax = l[0]
    for i in l:
        if i>max:
            smax = max
            max = i
    return smax


print(second_largest([2,5,7,3,15]))