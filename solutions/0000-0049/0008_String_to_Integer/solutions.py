class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
        
        sn = 1
        if s[0] == '-':
            sn = -1
            s = s[1:]
        elif s[0] == '+':
            sn = 1
            s = s[1:]
            
        ans = 0
        for ch in s:
            if not ch.isnumeric():
                break
            else:
                ans = 10 * ans + int(ch)
                
        ans *= sn
    
        if ans > 2**31-1:
            ans = 2**31-1
        
        if ans < -2**31:
            ans = -2**31
            
        return ans