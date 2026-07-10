class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1 
        res = float('-inf')
        while i < j:
            res = max(res, (j-i)*(min(heights[i], heights[j])))
            if heights[i] < heights[j]:
                i+=1 
            else:
                j-=1
        return res
        
            