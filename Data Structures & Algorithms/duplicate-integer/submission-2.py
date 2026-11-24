class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if num not in dup:
                dup[num] = True
            else:
                return True
        
        return False