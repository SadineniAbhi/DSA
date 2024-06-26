def rep_once(arr):
    ans = 0 
    for i in arr:
        ans = ans^ i 
    return ans
