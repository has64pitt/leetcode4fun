# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []
        
        dummy = head
        
        while dummy and dummy.next:
            even.append(dummy)
            odd.append(dummy.next)
            
            dummy = dummy.next.next

        if not odd:
            return dummy
        
        newhead = odd[0]
        
        for prev, nxt in zip(odd, even):
            prev.next = nxt
            nxt.next = None
            
        for prev, nxt in zip(even, odd[1:]):
            prev.next = nxt
        
        if dummy:
            even[-1].next = dummy
        
        return newhead
            