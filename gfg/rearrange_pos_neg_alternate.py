# An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and negative numbers are placed alternatively. A number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

def rerarrange(arr,n):
    i=-1
    for j in range(n):
        if arr[j]<0:
            i+=1
            arr[i],arr[j] =arr[j],arr[i]
    pos = i+1
    neg = 0

    while pos<n  and neg<pos and arr[neg]<0:
        arr[pos],arr[neg] =arr[neg],arr[pos]
        pos+=1
        neg+=2
    print(arr)

rerarrange([-3,-2,4,6,-7],5)