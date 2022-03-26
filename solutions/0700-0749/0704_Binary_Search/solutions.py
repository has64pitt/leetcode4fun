class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        
        left = 0
        right = N-1
        
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
                
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        
        return -1
        