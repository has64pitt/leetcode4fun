class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        
        def go(mid):
            return sum( (p-1) // mid  + 1 for p in piles) <= h
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if go(mid):
                right = mid
            else:
                left = mid
                
        if go(left):
            return left
        else:
            return right