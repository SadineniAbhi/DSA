def in_sort(arr):
    for i in range(len(arr)):
        j = i 
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1] , arr[j] = arr[j], arr[j-1]
            j-=1
    return arr
res = in_sort([200,12,8,3,1])
print(res)