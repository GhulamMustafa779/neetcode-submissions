class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        l = 0
        maxNum = max(nums[l: k])
        res.append(maxNum)

        for r in range(k, len(nums)):
            if nums[r] > maxNum and nums[l] != maxNum:
                res.append(nums[r])
                maxNum = nums[r]
            else:
                maxNum = max(nums[l + 1:r + 1])
                res.append(maxNum)
            
            l+=1
        return res
