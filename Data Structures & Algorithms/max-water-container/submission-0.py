class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            if heights[l] != 0 and heights[r] != 0:
                water = (r - l) * min(heights[l] , heights[r])
                maxWater = max(maxWater, water)
                
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1 
        
        return maxWater