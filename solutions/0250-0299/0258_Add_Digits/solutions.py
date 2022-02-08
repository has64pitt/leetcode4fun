class Solution:
    def addDigits(self, num: int) -> int:
        nums = str(num)
        
        while len(nums) > 1:
            ans = 0
            for ch in nums:
                ans += int(ch)
            nums = str(ans)
        
        return int(nums)