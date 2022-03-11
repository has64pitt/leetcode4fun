# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        dummy = head
        
        ct = 0
        tail = dummy
        while dummy:
            ct += 1
            tail = dummy
            dummy = dummy.next
            
            
        k %= ct
        
        if k == 0:
            return head
        
        
        dummy = head
        
        current = 1
        while current < ct-k:
            dummy = dummy.next
            current += 1
        
        newhead = dummy.next
        dummy.next = None
        tail.next = head
        
        return newhead