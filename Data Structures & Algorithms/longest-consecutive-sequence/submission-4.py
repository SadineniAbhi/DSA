class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        res = 0
        for i in range(len(nums)):
            cur = 0 
            for j in range(len(nums)):
                if nums[i] + j in unique_nums:
                    cur += 1 
                else:
                    break
            res = max(res, cur)
        return res