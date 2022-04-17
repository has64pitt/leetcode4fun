# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        def go(node):
            if node:
                return go(node.left) + [TreeNode(node.val)] + go(node.right)
            else:
                return []
            
        ans = go(root)
                    
        for prev, nxt in zip(ans, ans[1:]):
            prev.right = nxt
            
        return ans[0]