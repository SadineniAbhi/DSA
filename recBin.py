def recBin(arr,l,h,tar):
    mid = (l+h)//2
    if l>h:
        return "not present in the list"
    if arr[mid] == tar:
        return mid
    elif arr[mid] < tar:
        return recBin(arr,mid+1,h,tar)
    else:
        return recBin(arr,l,mid-1,tar)

print(recBin([1,2,3,4,5,10],0,5,90))
