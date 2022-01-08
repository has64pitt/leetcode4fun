from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        memo = {}
        def go(row, col1, col2):

            if row == rows:
                return 0
            
            if col1 > col2:
                col1, col2 = col2, col1
                
            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]
            
            ans = grid[row][col1]            
            if col1 != col2:
                ans += grid[row][col2]            
                
            best = 0
            for nxtCol1 in [col1-1, col1, col1+1]:                
                if 0 <= nxtCol1 < cols:
                    for nxtCol2 in [col2-1, col2, col2+1]:                    
                        if 0 <= nxtCol2 < cols:
                            current = go(row+1, nxtCol1, nxtCol2)
                            best = max(current, best)
                            
            memo[(row, col1, col2)] = ans + best
            return memo[(row, col1, col2)]
        
        ans = go(0, 0, cols-1)
        return ans