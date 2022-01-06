from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        ending = []
        current = 0
        
        for n, frm, to in trips:
            while ending and ending[0][0] <= frm:
                prevTo, prevN = heapq.heappop(ending)
                current -= prevN
                
            if current + n > capacity:
                return False
            else:
                heapq.heappush(ending, (to, n))
                current += n
                
        return True
                