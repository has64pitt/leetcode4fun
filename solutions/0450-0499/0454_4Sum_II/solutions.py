class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        
        lookup = collections.defaultdict(int)
        
        for num1 in nums1:
            for num2 in nums2:
                lookup[num1+num2] += 1
        
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                target = 0-num3-num4
                ans += lookup[target]
        
        return ans