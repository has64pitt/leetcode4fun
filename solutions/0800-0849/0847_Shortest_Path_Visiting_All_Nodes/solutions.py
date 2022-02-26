class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        
        N = len(graph)
        
        INF = 10**10
        dist = [ [INF] * N for _ in range(N) ]
        
        for node, neighbors in enumerate(graph):
            dist[node][node] = 0
            for nei in neighbors:
                dist[node][nei] = 1
                
        for start in range(N):
            for end in range(N):
                for mid in range(N):
                    dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
        
        best = 10**10

        #print(dist)
        memo = {}
        def go(node, mask):
            
            if mask == (1<<N) - 1:
                return 0
            
            if (node, mask) not in memo:
                best = INF
                for nxt in range(N):
                    if (1<<nxt) & mask == 0:
                        best = min(best,
                                   go(nxt, (1<<nxt) | mask) + dist[node][nxt]
                                  )
                memo[(node, mask)] = best
            return memo[(node, mask)]
        
        for start in range(N):
            current = go(start, 1<<start)
            best = min(best, current)
        return best
            