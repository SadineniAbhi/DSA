import math
def check(arr,mid):
    ans = 0
    for i in arr:
        ans += math.ceil(i/mid)
    return ans 


def binsearch(arr,k,mval):
    l = 1 
    h = mval
    while l<= h:
        mid = (l+h)//2 
        if check(arr,mid) == k:
            return mid 
        elif check(arr,mid) < k:
            h = mid - 1
        else:
            l = mid + 1 
arr =[25, 12, 8, 14, 19]
print(binsearch(arr,5,max(arr)))