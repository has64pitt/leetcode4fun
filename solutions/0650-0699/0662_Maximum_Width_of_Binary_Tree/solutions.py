# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append( (root, 0, 0)) # node, level, index
        
        best = 0
        
        while queue:
            qlen = len(queue)
            
            leftmost = float('inf')
            rightmost = 0
            
            for _ in range(qlen):
                node, level, index = queue.popleft()
                
                leftmost = min(leftmost, index)
                rightmost = max(rightmost, index)
            
                if node.left:
                    queue.append( (node.left, level+1, 2*index) )

                if node.right:
                    queue.append( (node.right, level+1, 2*index+1) )
            
            #print(leftmost, rightmost)
            best = max(best, rightmost - leftmost+1)
            
        return best