class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        if n % 2 == 1:
            return False
        
        
        # scan from left to right, how many fixed right-braket
        # right-braket <= left_braket
        right_fix = 0
        for index, (ch, lock) in enumerate(zip(s, locked)):
            if lock == '1' and ch == ')':
                right_fix += 1
                
            if right_fix > index+1- right_fix:
                return False

        # scan from right left, how many fixed left-braket
        # left-braket <= right_braket            
        left_fix = 0
        for index, (ch, lock) in enumerate(zip(s[::-1], locked[::-1])):
            if lock == '1' and ch =='(':
                left_fix += 1
            if left_fix > index+1-left_fix:
                return False
            
        return True

sol = Solution()

s = "))()))"
locked = "010100"
print(sol.canBeValid(s, locked))

