class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [i for i in candidates if i <= target]
        
        candidates.sort()
        

        N = len(candidates)
        
        ans = []
        
        def go(csum, current_list, current_index):
            if csum == target:
                ans.append(current_list[:])
                return
            
            for i in range(current_index, N):
                if csum + candidates[i] <= target:
                    go(csum + candidates[i], current_list + [candidates[i]], i)
        
        go(0, [], 0)
        
        return ans