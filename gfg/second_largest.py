def print2largest(arr, n):
		# code here
        max = arr[0]
        sec_max= -1
        for i in range(1,n):
            if arr[i]>max:
                sec_max = max
                max = arr[i]
            elif arr[i]>sec_max and arr[i]!=max:
                 sec_max = arr[i]
        return sec_max

print(print2largest([2,39,1,10,35,67],6))