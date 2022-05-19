class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = [[1] * n for _ in range(m)]
        
        stack = []
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                stack.append( (-val, i, j) )
                
        stack.sort()
        
        for val, x, y in stack:
            
            current = 1
            for dx, dy in [(0, 1), (0, -1), (1,0),(-1, 0)]:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] > matrix[x][y]:
                        current = max(current, 1 + ans[nx][ny])
        
            ans[x][y] = current
            
        return max(max(i) for i in ans)
    