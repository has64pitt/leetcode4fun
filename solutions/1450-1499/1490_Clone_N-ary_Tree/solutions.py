"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        
        
        def go(node):
            if not node:
                return node
            
            newnode = Node(node.val)
            
            if node.children:
                newnode.children = []
                for child in node.children:
                    newnode.children.append(go(child))
            
            return newnode
        
        
        ans = go(root)
        return ans