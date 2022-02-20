class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        

        
        N = len(intervals)
        ans = N
        
        mn, mx = intervals[0]
        for (l, r) in intervals[1:]:
            if l >= mn and r <= mx:
                ans -= 1
            else:
                mn = l
                mx = r
        
        return ans