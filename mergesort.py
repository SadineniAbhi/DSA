def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    lis = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            lis.append(arr[right])
            right += 1
        else:
            lis.append(arr[left])
            left += 1
    while left <= mid:
        lis.append(arr[left])
        left += 1

    while right <= high:
        lis.append(arr[right])
        right += 1

    for i in range(len(lis)):
        arr[low + i] = lis[i]

# Example usage
arr = [3, 1, 9, 2, 1, 222]
mergeSort(arr, 0, len(arr) - 1)






