class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        N = len(s)
        
        left = 0
        right = N-1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s1 = s[left+1:right+1]
                if s1 == s1[::-1]:
                    return True

                s1 = s[left:right]
                if s1 == s1[::-1]:
                    return True
                
                return False
        
        return True
                