# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(1000, head)
        
        prev = dummy
        
        prevVal = prev.val

        while prev.next:
            current = prev.next
            
            """
            can we keep current?
            
            if current.next is None
                yes
            elif current.val != current.next.val:
                yes
            else:
            
            """
            
            if current.next is None:
                return dummy.next
            elif current.val != current.next.val:
                prev = current
            else:
                val = current.val
                while current and current.val == val:
                    current = current.next
                prev.next = current
                
        return dummy.next
                
            
            
            
        
        