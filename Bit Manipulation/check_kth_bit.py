def check_kth_bit(k,n):
    if n&(1<<(k-1)):
        return True
    else:
        return False
    
print(check_kth_bit(2,1))