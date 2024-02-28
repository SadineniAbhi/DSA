def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j>0  and arr[j-1] >arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr

res = insertion_sort([22,33,54,3,4])
print(res)