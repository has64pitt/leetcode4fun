# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        def preOrder(node):
            return preOrder(node.left) + [node.val] + preOrder(node.right) if node else []
        
        tree1 = preOrder(root1)
        tree2 = preOrder(root2)
        
        N1 = len(tree1)
        N2 = len(tree2)
        
        p1 = p2 = 0
        
        ans = []
        
        while p1 < N1 and p2 < N2:
            if tree1[p1] < tree2[p2]:
                ans.append(tree1[p1])
                p1 += 1
            else:
                ans.append(tree2[p2])
                p2 += 1
        
        while p1 < N1:
            ans.append(tree1[p1])
            p1 += 1

        while p2 < N2:
            ans.append(tree2[p2])
            p2 += 1            
            
        return ans