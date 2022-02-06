class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        fast = slow = 0
        
        current = 10**10
        count = 0
        
        while fast < N:
            if nums[fast] == current:
                count += 1
            else:
                count = 1
                current = nums[fast]
                
            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        
        return slow