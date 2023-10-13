def rearrangeArray( nums):
    ans = [0]*len(nums)
    evenindex = 0
    negativeindex = 1
    for i in nums:
        print(i)
        if i>0:
            nums[evenindex] = i
            evenindex+=2
        else:
            nums[negativeindex] = i
            negativeindex+=2
    return ans

rearrangeArray([3,1,-2,-5,2,-4])