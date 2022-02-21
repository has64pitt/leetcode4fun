class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        N = len(nums)
        
        if N % 2 == 1:
            n = (N-1) // 2
            return nums[n]
        else:
            return nums[N//2]