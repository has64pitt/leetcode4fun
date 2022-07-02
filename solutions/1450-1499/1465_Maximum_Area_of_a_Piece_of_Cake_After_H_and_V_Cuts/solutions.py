class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        
        
        hmax = -1
        
        for prev, nxt in zip(horizontalCuts, horizontalCuts[1:]):
            hmax = max(hmax, nxt-prev)
            
        vmax = -1            
        for prev, nxt in zip(verticalCuts, verticalCuts[1:]):
            vmax = max(vmax, nxt-prev)            
            
        return hmax * vmax % (10**9+7)