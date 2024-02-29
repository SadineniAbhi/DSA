def selectionsort(arr):
    for i in range(len(arr)):
        minI = i
        for j in range(i,len(arr)):
            if arr[minI]>arr[j]:
                minI = j
        arr[minI],arr[i] = arr[i],arr[minI]
    return arr 

res = selectionsort([100,11,78,1,23])
print(res)

