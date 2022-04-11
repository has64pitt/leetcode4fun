class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        k %= (m*n)
        
        if k == 0:
            return grid
        
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m*n):
            index = i + k
            index %= (m*n)
            
            rold = i // n
            cold = i % n
            
            r = index // n
            c = index % n
            ans[r][c] = grid[rold][cold]
            
        return ans