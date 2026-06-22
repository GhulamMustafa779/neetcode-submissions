class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd, rightProd = [], []

        mul = 1
        for i in range(len(nums)):
            mul = nums[i] * mul
            leftProd.append(mul)
        
        mul = 1
        for j in range(len(nums)-1,-1,-1):
            mul = nums[j] * mul
            rightProd.insert(0, mul)
        
        res = []
        left, right = 0, 0 
        for k in range(len(nums)):
            if k - 1 >= 0:
                left = leftProd[k - 1]
            else:
                left = 1

            if k + 1 > len(nums) - 1:
                right = 1
            else:
                right = rightProd[k + 1]
            
            res.append(left * right)

        return res

