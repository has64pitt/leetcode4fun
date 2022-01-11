# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:                
        
        ans = 0
        
        def go(node, current):
            nonlocal ans
            if node:
                current = current * 2 + node.val
                if not node.left and not node.right:
                    ans += current

                go(node.left, current)
                go(node.right, current)
                        
        go(root, 0)
        return ans