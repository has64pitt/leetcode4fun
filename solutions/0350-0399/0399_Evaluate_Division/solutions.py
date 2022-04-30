class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        lookup = collections.defaultdict(set)
        
        for (x, y), val in zip(equations, values):
            
            lookup[x].add((y, val))                        
            lookup[y].add((x, 1.0/val))
                
                
        ans = []
        
        def go(x, y):
            if x not in lookup:
                return -1
            

            stack = [(x, 1)]
            seen = set()
            seen.add(x)

            
            while stack:
                var, val = stack.pop()
                for k, v in lookup[var]:
                    if k == y:
                          return val * v
                    
                    if k not in seen:
                        seen.add(k)
                        stack.append( (k, val*v) )
            
            return -1
                    
                    
                
        
        for x, y in queries:
            ans.append(go(x, y))
        
        return ans