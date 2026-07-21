class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = None
        n2 = None
        c1 = 0
        c2 = 0

        # Find candidates
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        # Verify candidates
        c1 = 0
        c2 = 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1

        ans = []
        if c1 > len(nums) // 3:
            ans.append(n1)
        if c2 > len(nums) // 3:
            ans.append(n2)

        return ans