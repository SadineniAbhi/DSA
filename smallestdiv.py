import math
def smallestDivisor(nums ,threshold):
    def sum_function(nums,div):
        s = 0 
        for i in range(len(nums)):
            s = math.ceil(nums[i]/div)

    def binsearch(l,h,arr):
        while l<= h:
            ans = max(arr)
            mid = (l+h)//2 
            res = sum_function()
            if  res <= threshold:
                h = mid - 1 
            else:
                l = mid + 1 
        return l 
