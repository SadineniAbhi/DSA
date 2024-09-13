import math
def check(arr,k):
    count = 0
    for i in arr:
        if i < k:
            count+=1 
    return count

def binsearch(arr,k,mval):
    l = 1 
    h = mval
    while l<= h:
        mid = (l+h)//2 
        if check(arr,mid) == k:
            return mid 
        elif check(arr,mid) > k:
            h = mid - 1
        else:
            l = mid + 1 
    return -1
print(binsearch(arr,5,max(arr)))