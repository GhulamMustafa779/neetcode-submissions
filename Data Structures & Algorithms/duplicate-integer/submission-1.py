class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        for num in nums:
            if num in dupMap:
                return True
            else:
                dupMap[num] = True
        
        return False