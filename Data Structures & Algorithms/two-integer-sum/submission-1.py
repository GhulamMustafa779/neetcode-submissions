class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums):
            if num in index:
                return [index[num], i]
            else:
                index[target-num] = i