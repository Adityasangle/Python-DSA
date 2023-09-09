def odd(x):
    if x%2!=0:
        return x

odds = list(filter(odd,[1,2,3,4,5]))
print(odds)