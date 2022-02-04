class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        N = len(nums)        
        

        lookup = {}
        lookup[0] = -1
        
        best = 0
        ones = 0
        
        for i in range(N):

            total_elements = i+1
            ones += nums[i]
            zeros = total_elements - ones
            dif = ones - zeros
            
            if dif not in lookup:
                lookup[dif] = i
            else:
                best = max(best, i - lookup[dif])
            
        
        
        return best
