class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def go(s1):
            ans = []
            
            for ch in s1:
                if ch != '#':
                    ans.append(ch)
                elif ans:
                    ans.pop()
            
            return ''.join(ans)
        
        s = go(s)
        t = go(t)
        
        return s == t