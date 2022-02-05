# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        queue = []
        
        k = len(lists)
        
        for i in range(k):
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy = ListNode()
        current = dummy
        
        while queue:
            val, nodeindex = heapq.heappop(queue)
            current.next = ListNode(val)
            current = current.next

            if lists[nodeindex]:
                heapq.heappush(queue, (lists[nodeindex].val, nodeindex))
                lists[nodeindex] = lists[nodeindex].next

                
        return dummy.next