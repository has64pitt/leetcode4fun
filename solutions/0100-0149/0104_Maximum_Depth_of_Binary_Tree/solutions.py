# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        ans = 0
        
        def go(node, current):
            nonlocal ans
            if node:
                current += 1
                
                ans = max(ans, current)
                go(node.left, current)
                go(node.right, current)
                
        go(root, 0)
        return ans