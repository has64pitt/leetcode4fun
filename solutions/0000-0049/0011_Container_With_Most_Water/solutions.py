class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        
        left = 0
        right = N-1
        
        best = -1
        
        while left < right:
            current =  min(height[right], height[left]) * (right-left)
            best = max(best, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return best
            