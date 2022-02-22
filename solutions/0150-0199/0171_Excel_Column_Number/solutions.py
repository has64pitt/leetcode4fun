class Solution:
    def titleToNumber(self, s: str) -> int:
        N = len(s)
        
        ans = 0
        
        for ch in s:
            num = ord(ch) - ord('A') + 1

            ans = 26 * ans + num
            
        return ans