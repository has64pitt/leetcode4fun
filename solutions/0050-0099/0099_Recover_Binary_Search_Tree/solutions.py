# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.swapFound = 0
        self.leftNode = None
        self.rightNode = None
        self.pred = None
        
        def inorder(node):
            if node:
                inorder(node.left)
        
                if self.pred and self.pred.val > node.val:
                    if self.swapFound == 0:
                        self.leftNode = self.pred
                        self.rightNode = node
                        self.swapFound += 1
                    else:
                        self.rightNode = node
                        
                self.pred = node
                
                inorder(node.right)
                
        inorder(root)
                
        self.leftNode.val, self.rightNode.val = self.rightNode.val, self.leftNode.val