class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        size = len(nums)
        res = [1] * size
        for i in range(size):
            res[i] *= prefix
            prefix *= nums[i]
            res[size-1-i] *= postfix
            postfix *= nums[size-1-i]
        
        return res