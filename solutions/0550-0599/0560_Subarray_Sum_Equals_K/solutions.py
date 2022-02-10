class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
              
        ct = collections.defaultdict(int)
        ct[0] = 1
        
        ans = 0
        
        current = 0
        for i in range(N):
            current += nums[i]
            target = current - k
            ans += ct[target]            
            ct[current] += 1
            
        return ans
            