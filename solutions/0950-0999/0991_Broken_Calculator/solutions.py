class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        
        
        ans = 0
        
        while target > startValue:
            if target % 2 == 1:
                ans += 1
                target += 1
            
            target = target // 2
            ans += 1
            
        return ans + startValue - target
        