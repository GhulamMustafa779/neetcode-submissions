class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in map.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result