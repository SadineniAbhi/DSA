def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

res = bubblesort([2,6,1,11,5,3])

print(res)
