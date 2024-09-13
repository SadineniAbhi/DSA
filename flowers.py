from typing import List
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay)<k:
        return -1 
    
    def check(curDay):
        res = 0
        count = 0 
        for i in bloomDay:
            if i <= curDay:
                count+=1 
            else:
                count = 0 
            if count>=k:
                res+=1 
        return res 
    
    def binarysearch(l,h):
        ans = -1 
        while l<=h:
            mid = (l+h)//2 
            if check(mid)>= m:
                ans = mid 
                h = mid -1 
            else:
                l = mid + 1 
        return ans 
    
    return binarysearch(1,max(bloomDay))
            



