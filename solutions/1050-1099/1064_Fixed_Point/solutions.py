class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        
        N = len(arr)
        
        left = 0
        right = N-1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if arr[mid] >= mid:
                right = mid
            elif arr[mid] < mid:
                left = mid
                
        if arr[left] == left:
            return left
        elif arr[right] == right:
            return right
        
        return -1