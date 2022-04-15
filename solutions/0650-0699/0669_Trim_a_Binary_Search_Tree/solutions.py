# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def go(node):
            if not node:
                return None
            else:
                if node.val > high:
                    return go(node.left)
                elif node.val < low:
                    return go(node.right)
                else:
                    node.left = go(node.left)
                    node.right = go(node.right)
                    return node
                
        return go(root)