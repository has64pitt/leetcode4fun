class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        lookup = collections.defaultdict(list)
        
        for frm, to, t in times:
            lookup[frm].append((to, t))
            
        current_time = 0
        seen = set()
        
        stack = [(0, k)]
        
        while stack:                
            current_time, current_node = heapq.heappop(stack)
            
            if current_node not in seen:
                seen.add(current_node)
        
            if len(seen) == n:
                return current_time
            
            for nxt, t in lookup[current_node]:
                if nxt not in seen:
                    heapq.heappush(stack, (current_time + t, nxt))
            
        return -1