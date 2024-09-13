
def f_l_m(nums,target):

    l = 0 
    h = len(nums)-1 
    index = -1

    while l<=h:
        mid = (l+h)//2
        if nums[mid] == target:
            index = mid 
            h = mid -1 
        elif nums[mid] > target:
            h = mid - 1 
        else:
            l = mid + 1 
    return index 



def f_r_m(nums,target):

    l = 0 
    h = len(nums)-1 
    index = -1

    while l<=h:
        mid = (l+h)//2
        if nums[mid] == target:
            index = mid 
            l = mid + 1
        elif nums[mid] > target:
            h = mid - 1 
        else:
            l = mid + 1 
    return index 

