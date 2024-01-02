def stock_buysell(arr,n):
    profit = 0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit

print(stock_buysell([7,1,4,3,9],5))