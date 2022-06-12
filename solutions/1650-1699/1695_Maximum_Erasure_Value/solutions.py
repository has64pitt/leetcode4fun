class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        best = -1
        
        preSum = [0] * (N+1)       
        for i in range(N):
            preSum[i+1] = preSum[i] + nums[i]
                        
        lookup = {}        
        current = 0
        startIndex = 0
        
        for index, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = index
                current = preSum[index+1] - preSum[startIndex]
                best = max(best, current)
            else:
                startIndex = max(lookup[num] + 1, startIndex)
                current = preSum[index+1] - preSum[startIndex]
                best = max(best, current)
                lookup[num] = index
                
        return best
                
                
            