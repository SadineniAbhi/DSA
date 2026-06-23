class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = [] 
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                prod = prod * nums[i]
        if zeros != []:
            res = [0] * len(nums)
            if len(zeros) > 1:
                prod = 0
            for zero_index in zeros:
                res[zero_index] = prod 
            return res
        res = [prod]* len(nums)
        for i in range(len(res)):
            res[i] = prod // nums[i]
        return res