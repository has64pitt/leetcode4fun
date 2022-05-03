class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numssorted = sorted(nums)
        
        mn = None
        mx = None
        
        for index, (n1, n2) in enumerate(zip(nums, numssorted)):
            if n1 == n2:
                continue
            else:
                if mn is None:
                    mn = index
                else:
                    mx = index
                    
        if mx is None and mn is None:
            return 0
        
        elif mx is None:
            return 1
        
        return mx - mn + 1
                