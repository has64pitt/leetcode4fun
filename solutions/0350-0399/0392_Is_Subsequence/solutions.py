class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1 = len(s)
        N2 = len(t)
        
        if N1 > N2:
            return False
        
        p1 = 0
        p2 = 0
        
        while p1 < N1 and p2 < N2:
            if s[p1] == t[p2]:
                p1 += 1
            
            p2 += 1
            
        return p1 == N1
                
        