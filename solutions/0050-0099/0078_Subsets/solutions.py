class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        
        ans = []
        for mask in range(1<<N):
            current = []
            for index in range(N):
                if mask & (1<<index):
                    current.append(nums[index])
            ans.append(current)
            
        return ans
                