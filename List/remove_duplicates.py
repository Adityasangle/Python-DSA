def remove_duplicates(arr,n):
    i=0
    for j in range(n-1):
        if arr[j]!=arr[j+1]:
            arr[i]=arr[j]
            i+=1
    arr[i]=arr[n-1]
    return i+1


l= [int(x) for x in input().split()]
new_l = remove_duplicates(l,len(l))
for i in range(new_l):
    print(l[i],end= " ")