class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minSpeed = float('inf')
        while l <= r:
            mid = (l+r+1) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)

            if total <= h:
                minSpeed = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return minSpeed
