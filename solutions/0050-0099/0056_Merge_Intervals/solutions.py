from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort intervals by start, if start is same, it does not matter whether end is inc or decs
        Time O(NlogN)
        Space O(N)
        """
        intervals.sort()
        
        res = []
        
        for start, end in intervals:
            if not res:
                res.append([start, end])
            elif res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
                
        return res



sol = Solution()

print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))

