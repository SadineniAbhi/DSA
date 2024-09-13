def floor(arr,k):
    l = 0 
    h = len(arr)
    arr.sort()
    ans = -1
    while l<h:
        mid = (l+h)//2
        if arr[mid]>k:
            l = mid+1 
        
        elif arr[mid] <= k:
            ans = arr[mid]
            l = mid + 1 
    return ans

print(floor([1,2,3,4],5))
