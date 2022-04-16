# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def go(node, add):
            if node:
                
                val = go(node.right, add)
                
                node.val += val
                
                val = go(node.left, node.val)
                
                return val
            else:
                return add
                
                
        
        go(root, 0)
    
        return root
    
                