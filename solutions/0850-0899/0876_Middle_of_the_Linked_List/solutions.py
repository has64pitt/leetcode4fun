# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        fast = slow = dummy
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow.next

