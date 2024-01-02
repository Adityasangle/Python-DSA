def stock_buy_sell(arr,n):
    i=0
    j=1
    n=len(arr)
    max_profit = 0
    while i<n and j<n:
        if arr[j]<arr[i]:
            i=j
            j+=1
        else:
            diff = arr[j]-arr[i]
            max_profit = max(max_profit,diff)
            j+=1
    return max_profit

print(stock_buy_sell([7,1,6,3,9],5))
