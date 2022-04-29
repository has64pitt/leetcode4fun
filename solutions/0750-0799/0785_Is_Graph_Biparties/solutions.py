class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        N = len(graph)
        
        stack = []
        
        for index, nodes in enumerate(graph):
            stack.append( (len(nodes), index, nodes ) )
            
        stack.sort(key = lambda x: (-x[0], x[1]))
        
        
        startNode = stack[0][1]
        stack = [(startNode, 0)]
        
        lookup = {}
        lookup[startNode] = 0
        
        while stack:
            node, tp = stack.pop()
            for nxt in graph[node]:
                if nxt not in lookup:
                    lookup[nxt] = 1 - tp
                    stack.append((nxt, 1-tp))
                else:
                    if lookup[nxt] == tp:
                        return False
        
        return True
            