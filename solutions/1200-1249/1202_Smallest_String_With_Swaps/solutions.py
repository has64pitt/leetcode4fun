class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        N = len(s)
        
        uroot = {i:i for i in range(N)}
        
        
        def ufind(x):
            if uroot[x] != x:
                uroot[x] = ufind(uroot[x])
            
            return uroot[x]
        
        def uunion(x, y):
            xroot = ufind(x)
            yroot = ufind(y)
            
            if xroot != yroot:
                uroot[xroot] = yroot
        
        for a, b in pairs:
            aroot = ufind(a)
            broot = ufind(b)
            
            if aroot != broot:
                uunion(a, b)
            
            
        for i in range(N):
            ufind(i)
            
        lookuppos = collections.defaultdict(list)
        lookupchs = collections.defaultdict(list)
        for k, v in uroot.items():
            lookuppos[v].append(k)
            lookupchs[v].append(s[k])
                    
                
        ans = [None] * N
        
        for k in lookuppos.keys():
            s1 = sorted(lookupchs[k])
            p1 = sorted(lookuppos[k])
            for pos, ch in zip(p1, s1):
                ans[pos] = ch
                
        return ''.join(ans)
        
        