class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        N = len(prices)
        
        best = 0
        mn = None
        for price in prices:
            if mn is None:
                mn = price
            else:
                current = price - mn
                best = max(best, current)
                if price < mn:
                    mn = price
                    
        return best