class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(10**4)]
        c = {}

        for num in nums:
            c[num] = c.get(num, 0) + 1

        for val, count in c.items():
            res[count].append(val)
        ans = []
        for i in res[::-1]:
            if len(ans)>=k:
                break
            if i != []:
                ans.extend(i)
        return ans