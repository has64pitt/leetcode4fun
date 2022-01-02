from typing import Collection


class Solution:
    def numPairsDivisibleBy60(self, durations: List[int]) -> int:
                
        ct = Collection.defaultdict(int)
        
        ans = 0
        
        for duration in durations:
            duration %= 60
            
            target = 60 - duration
            target %= 60
            
            ans += ct[target]
            ct[duration] += 1
            
        return ans