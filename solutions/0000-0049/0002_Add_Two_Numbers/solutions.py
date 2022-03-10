# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(0)
        dummy = ans
        rd = 0
        
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            v = v1 + v2 + rd
            
            if v >= 10:
                v -= 10
                rd = 1
            else:
                rd = 0
                
            ans.next = ListNode(v)
            ans = ans.next
            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            v1 = l1.val
            
            v = v1 + rd
            
            if v >= 10:
                v -= 10
                rd = 1
            else:
                rd = 0
                
            ans.next = ListNode(v)
            ans = ans.next
            l1 = l1.next
            
        while l2:
            v2= l2.val
            
            v = v2+ rd
            
            if v >= 10:
                v -= 10
                rd = 1
            else:
                rd = 0
                
            ans.next = ListNode(v)
            ans = ans.next
            l2= l2.next            
            
        if rd:
            ans.next = ListNode(1)
            
        return dummy.next