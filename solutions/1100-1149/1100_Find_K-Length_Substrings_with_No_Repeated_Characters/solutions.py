class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        
        N = len(s)
        
        if k > N:
            return 0
        
        
        ans = 0
        lookup = collections.defaultdict(int)
        ct = 0
        
        for index, char in enumerate(s):
            lookup[char] += 1
            
            if lookup[char] == 1:
                ct += 1
                
            if index >= k:
                prev = s[index - k]
                lookup[prev] -= 1
                if lookup[prev] == 0:
                    ct -= 1
            
            if ct == k:
                ans += 1
            
        return ans