# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        def dfs(node):
            if node:
                return dfs(node.left) + [node.val] + dfs(node.right)
            else:
                return []
            
        self.stack = dfs(root)
        self.index = 0
        self.length = len(self.stack)
        
    def next(self) -> int:
        val = self.stack[self.index]
        self.index += 1
        return val
        

    def hasNext(self) -> bool:
        return self.index < self.length
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()