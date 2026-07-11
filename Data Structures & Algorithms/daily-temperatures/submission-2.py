class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        stack = []
        stack.append(0)

        for i in range(1, size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                num = i - stack[-1]
                res[stack[-1]] = num
                stack.pop()

            stack.append(i)

        return res
