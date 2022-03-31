class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        
        if m == N:
            return max(nums)
        
        left = max(nums)
        right = sum(nums)
        
        def can_do_with_largest_sum(mid):
            current = 0
            ct = 1
            
            for num in nums:
                if current + num > mid:
                    current = num
                    ct += 1
                else:
                    current += num
        
            return ct <= m
            
        
        while left + 1 < right:
            mid = (left + right) // 2
            if can_do_with_largest_sum(mid):
                right = mid
            else:
                left = mid
                
        if can_do_with_largest_sum(left):
            return left
        else:
            return right