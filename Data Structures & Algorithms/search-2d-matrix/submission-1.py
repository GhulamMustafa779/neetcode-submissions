class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        i = 0
        while i < r:
            if target >= matrix[i][0] and target <= matrix[i][c - 1]:
                l = 0
                r = c - 1
                while l <= r:
                    mid = (l + r + 1) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
            i += 1
        
        return False