# left most and right most element in bin search algo 


def floor(arr,q):
    l = 0 
    h = len(arr)-1 
    while l<=h:
        mid = (l+h)//2
        if arr[mid]> q:
            h = mid -1 
        elif arr[mid] <=q:
            cur = arr[mid]
            l = mid+1 
    return cur 

def ceil(arr,q):
    cur = -10e8
    l = 0 
    h = len(arr)-1 
    while l <=h:
        mid = (l+h)//2
        if arr[mid] >= q:
            cur = arr[mid]
            h = mid -1 
        elif arr[mid]<q:
            l = mid+1    
    return cur 

def leftmost(arr,q):
    index = -1 
    l = 0 
    h = len(arr)-1 
    while l <=h:
        mid = (l+h)//2
        if arr[mid] < q:
            l = mid+1 
        elif arr[mid] == q:
            h = mid - 1
            index = mid 
        else :
            h = mid - 1 
    return index 


def rightmost(arr,q):
    index = -1 
    l = 0 
    h = len(arr)-1 
    while l<=h:
        mid = (l+h)//2
        if arr[mid] > q:
            h = mid -1 
        elif arr[mid] == q:
            l = mid+1 
            index = mid 
        else:
            l = mid+1 
    return index