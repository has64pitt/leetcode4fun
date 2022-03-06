class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def go(i):
            if i == 1:
                return 1
            else:
                return go(i-1) * i * (2*i-1) 
            
        
        return go(n) % MOD