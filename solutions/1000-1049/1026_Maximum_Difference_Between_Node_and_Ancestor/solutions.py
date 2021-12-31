# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        
        
        def go(node):
            if node:
                nonlocal ans
                
                if node.left:
                    leftmin, leftmax = go(node.left)
                else:
                    leftmin = float('inf')
                    leftmax = float('-inf')
                if node.right:
                    rightmin, rightmax = go(node.right)
                else:
                    rightmin = float('inf')
                    rightmax = float('-inf')
                    
                mn = min(leftmin, rightmin)
                mx = max(leftmax, rightmax)
                
                if mn < float('inf'):
                    ans = max(ans, abs(mn - node.val))
                if mx > float('-inf'):
                    ans = max(ans, abs(mx - node.val))
                
                return min(mn, node.val), max(mx, node.val)
            
            else:
                return -1, -1
                
        go(root)
        
        return ans