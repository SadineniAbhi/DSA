class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        dic = {0: 1}
        prefix = []
        psum = 0 
        for num in nums:
            psum += num
            prefix.append(psum)

        for i in range(len(prefix)):
            target = prefix[i] - k 
            if target in dic:
                res += dic[target]
            dic[prefix[i]] = dic.get(prefix[i], 0)  + 1
        return res