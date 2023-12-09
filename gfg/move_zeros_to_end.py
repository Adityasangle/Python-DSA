def pushZerosToEnd(arr, n):
    	# code here
    nonzeroidx = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonzeroidx],arr[i] = arr[i],arr[nonzeroidx]
            nonzeroidx+=1
    while nonzeroidx != len(arr):
            arr[nonzeroidx] = 0 
            nonzeroidx+=1
    print(arr)

pushZerosToEnd([0,0,3,0,4,5,6],7)
