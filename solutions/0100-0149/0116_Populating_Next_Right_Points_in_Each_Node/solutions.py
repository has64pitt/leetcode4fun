# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def go(node1, node2):
            if not node1:
                return 
            
            else:
                go(node1.left, node1.right)
                go(node1.right, node2.left)
                go(node2.left, node2.right)
                
                node1.next = node2
                return
            
        go(root.left, root.right)
        
        return root