class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkMap = {}
        for i in range(len(nums)):
            if nums[i] not in checkMap:
                checkMap[target - nums[i]] = i
            else:
                return [checkMap[nums[i]], i]
