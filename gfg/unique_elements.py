from collections import Counter

def get_unique(arr,n):
    cntr = dict(Counter(arr))
    d = sorted(cntr.items(),key = lambda x:x[1])
    print(d)
    uniques = []
    for key,val in cntr.items():
        if val==1:
            uniques.append(key)
    print(uniques)
get_unique([2,1,2,3,4,5,4,6,6],9)