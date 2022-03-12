"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodelist = []
        
        if not head:
            return head
        
        nodedict = {}        
        index = 0
        while head:
            nodelist.append( (head, head.random))            
            nodedict[head] = index            
            index += 1
            head = head.next
            
            
                    
        
        newnodedict = {}
        def getnode(index):
            if index not in newnodedict:
                newnodedict[index] = Node(nodelist[index][0].val)
            
            return newnodedict[index]
            
        
        ans = []
        for index, (node, randomnode) in enumerate(nodelist):
            newnode = getnode(index)
            if randomnode is not None:
                newrandomnode = getnode(nodedict[randomnode])
                newnode.random = newrandomnode
                
            ans.append(newnode)
        
        for pnode, nnode in zip(ans, ans[1:]):
            pnode.next = nnode
        
        return ans[0]
            
        
        