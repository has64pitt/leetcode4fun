class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack = []
        
        for s in stones:
            heapq.heappush(stack, -s)
            
        while len(stack) > 1:
            a = heapq.heappop(stack)
            b = heapq.heappop(stack)
            
            a *= -1
            b *= -1
            
            left = a - b
            if left > 0:
                heapq.heappush(stack, -left)
            
        if stack:
            return -stack[0]
        else:
            return 0