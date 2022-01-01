class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if len(set(nums)) == 1:
            num = nums[0]
            if len(nums) == 1:
                return num
            elif len(nums) == 2:
                return num ** 2 + num
            else:
                n = len(nums)
                return (n-2) * (num ** 3) + num ** 2 + num
        
        nums = [1] + nums + [1]
        
        N = len(nums)

        memo = {}        
        def go(left, right): # inclusive            
            if left > right:
                return 0
            elif left == right:
                return nums[left-1] * nums[left] * nums[right+1]
            else:
                if (left, right) not in memo:
                    ans = float('-inf')
                    for i in range(left, right+1):
                        current = nums[left-1] * nums[right+1] * nums[i]
                        current += go(left, i-1) 
                        current += go(i+1, right)
                        ans = max(ans, current)
                    
                    memo[(left, right)] = ans
                return memo[(left, right)]
                    
        
        ans = go(1, N-2)

        return ans

"""
Time is O(N^3)
Space is O(N^2)
"""