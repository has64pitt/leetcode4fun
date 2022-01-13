class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[1]))
        #print(points)
        ans = 0
        prev_end = None
        
        for start, end in points:
            if not prev_end or start > prev_end:
                prev_end = end
                ans += 1
            
        return ans
            