def minimum_platforms(arr,dep):
    i = 1
    j =0
    plat_occ = 1
    max_plat = 1
    n = len(arr)
    arr = sorted(arr)
    dep = sorted(dep)
    while i<n and j<n:
        if arr[i]-dep[j]>0:
            plat_occ-=1
            j+=1 
        else:
            plat_occ+=1
            i+=1
        max_plat = max(max_plat,plat_occ)
    return max_plat

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(minimum_platforms(arr,dep))