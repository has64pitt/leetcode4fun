class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        stack = []
        
        N = len(costs)
        n = N // 2
        
        for index, (a, b) in enumerate(costs):
            absdif = abs(a - b)
            heapq.heappush(stack, (-absdif, a, b, index))
            
        
        acount = 0
        bcount = 0
        
        ans = 0
        
        while acount < n and bcount < n and stack:
            absdif, a, b, index = heapq.heappop(stack)
            
            ans += min(a, b)
            
            if a < b:
                acount += 1
            elif a > b:
                bcount += 1
                
        if acount == n:
            while stack:
                absdif, a, b, index = heapq.heappop(stack)            
                ans += b
        else:
            while stack:
                absdif, a, b, index = heapq.heappop(stack)            
                ans += a
                
        return ans