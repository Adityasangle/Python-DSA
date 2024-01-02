def longest_oddeven(arr,n):
    longest = 1
    count = 1
    for i in range(1,n):
        if (arr[i]%2==0 and arr[i-1]%2!=0) | (arr[i]%2!=0 and arr[i-1]%2==0):
            count+=1
            longest = max(longest,count)
        else:
            count=1

    return longest


print(longest_oddeven([2,4,5,6,9,12],6))