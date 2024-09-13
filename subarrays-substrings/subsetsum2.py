from typing import List





def subsetsWithDup( nums: List[int]) -> List[List[int]]:
    ans = []
    ds = []


    def findSubsets(ind: int):
        ans.append(ds[:])
        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i - 1]:
                continue
            ds.append(nums[i])
            findSubsets(i + 1)
            ds.pop()
    nums.sort()
    findSubsets(0)
    return ans


nums = [1, 2, 2]
subsetsWithDup(nums)