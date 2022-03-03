class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        

        
        current_diff = None
        current_ct = 0
        
        
        
        ans = 0
        
        for prev, nxt in zip(nums, nums[1:]):
            diff = nxt - prev
            
            if current_diff is None or current_diff == diff:
                current_diff = diff
                current_ct += 1
            else:
                ans += current_ct * (current_ct - 1) // 2
                current_diff = diff
                current_ct = 1
                
        ans += current_ct * (current_ct - 1) // 2
        
        return ans