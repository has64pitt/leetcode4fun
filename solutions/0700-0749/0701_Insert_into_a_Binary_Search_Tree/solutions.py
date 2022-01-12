# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def go(node):
            if not node:
                return TreeNode(val)
            
            else:
                if node.val > val:
                    node.left = go(node.left)
                else:
                    node.right = go(node.right)
                
                return node
                    
        return go(root)