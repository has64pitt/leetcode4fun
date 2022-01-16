from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        N = len(seats)
        
        taken = [index for index, val in enumerate(seats) if val == 1]
        
        best = 0
        
        if taken[0] != 0:
            best = taken[0]
        
        if taken[-1] != N-1:
            best = max(best, N-1-taken[-1])

        for prev, nxt in zip(taken, taken[1:]):
            mid = (prev + nxt) // 2
            current = min(mid - prev, nxt - mid)
            best = max(best, current)
            
        return best
            
sol = Solution()

seats = [1,0,0,0,1,0,1]
print(sol.maxDistToClosest(seats))

seats = [1,0,0,0]
print(sol.maxDistToClosest(seats))

seats = [0,1]
print(sol.maxDistToClosest(seats))

seats = [1,0,0,1]
print(sol.maxDistToClosest(seats))