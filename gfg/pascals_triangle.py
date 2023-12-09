#print r rows and cs column element
def getPascalEle(r,c):
    r = r-1
    c = c-1
    res = 1
    for i in range(c): #to go till last c times, as c in denominator
        res = res*(r-i)
        res = res//(i+1)
    return res

print(getPascalEle(6,2))

def getRowOfPascal1(n):
    res = []
    for i in range(1,n+1):
        res.append(getPascalEle(n,i))
    return res


def getRowOfPascal2(n):
    res = 1
    ans = []
    ans.append(1)
    for i in range(1,n):
        res = res*(n-i)
        res= res//i
        ans.append(res)
    return ans



res = getRowOfPascal2(5)
print(res)

#print whole pascal traingale till n rows
def printPascal(n):
    triangle = []
    for row in range(1,n+1):
        triangle.append(getRowOfPascal2(row))
    return triangle

print(printPascal(4))
