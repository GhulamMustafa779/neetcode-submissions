# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(root):
            if not root:
                return 0
            
            left = 1 + findDepth(root.left)
            right = 1 + findDepth(root.right)

            if left >= right:
                return left
            else:
                return right

        maxD = findDepth(root) 
        return maxD