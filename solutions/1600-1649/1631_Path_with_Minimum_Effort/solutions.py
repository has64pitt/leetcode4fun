class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        left = 0
        right = 10**6
        
        m = len(heights)
        n = len(heights[0])
        
        def go(num):
            stack = [(0,0)]
            seen = set()
            seen.add((0,0))
            
            while stack:
                x, y = stack.pop()
                if x == m-1 and y == n-1:
                    return True
                
                for dx, dy in [(1,0), (-1, 0), (0,1), (0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(heights[nx][ny] - heights[x][y]) <= num:
                        

                
                        stack.append((nx, ny))
                        seen.add((nx, ny))
                
            return False
            
        
        
        while left + 1 < right:
            mid = (left + right) // 2
            if go(mid):
                right = mid
            else:
                left = mid
                
        if go(left):
            return left
        else:
            return right