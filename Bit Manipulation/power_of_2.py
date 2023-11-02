#to check if power of 2
#n%(n-1) sets the last set bit to 0, and if there is only one bit set its a power of 2,
# so if we check n&(n-1) == 0 , we will get if its a power of 2
def powerOf2(n):
    if n&(n-1) == 0:
        return True
    else:
        return False

print(powerOf2(15))