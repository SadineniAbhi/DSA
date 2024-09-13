def recbin(arr,l, h,k):
    if l>h:
        return
    mid =(l+h)//2
    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        h = m -1 
        return recbin(arr,l,h,k)
    
    l = m+1
    return recbin(arr,l,h,k)
print(recbin([1,2,3,4,5,6],0,6,4))