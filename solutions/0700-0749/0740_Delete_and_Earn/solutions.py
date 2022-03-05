class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ct = collections.Counter(nums)
        
        keys = sorted(list(ct.keys()))
        
        #print(keys, ct)
        
        N = len(keys)
        
        ans = [0] * (N+1)
        
        for index in range(N-1, -1, -1):
            k = keys[index]
            if index == N-1:
                ans[index] = k * ct[k]
            else:
                nk = keys[index+1]
                if nk != (k+1):
                    ans[index] = k * ct[k] + ans[index+1]
                else:
                    ans[index] = max(k * ct[k] + ans[index+2], 
                                     ans[index+1])
        
        #print(ans)
        return ans[0]