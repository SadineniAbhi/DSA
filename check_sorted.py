def check_sorted(arr,i):
    if i == len(arr)-1:
        return True 
    if arr[i]>arr[i+1]:
        return False 

    return check_sorted(arr,i+1)

print(check_sorted([1,3,6,7,91,10],0))