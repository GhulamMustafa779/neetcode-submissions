class Solution:
    def trap(self, height: List[int]) -> int:
        minH = [0] * len(height)
        rMax = 0
        for i in range(len(height)-1,-1,-1):
            minH[i] = rMax
            rMax = max(height[i], rMax)
        
        lMax = 0
        water = 0
        for i in range(len(height)):
            water += max(0, min(lMax, minH[i]) - height[i])
            lMax = max(lMax, height[i])
        
        return water