class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in nums:
                continue
            else:
                counter = 0
                num = nums[i]
                while num in nums:
                    num += 1
                    counter +=1
                longest = max(longest, counter)

        return longest