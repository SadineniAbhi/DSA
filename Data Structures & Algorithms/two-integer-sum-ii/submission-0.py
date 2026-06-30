class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {} # {val: ind}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]]+1, i +1]
            dic[target - numbers[i]] = i
