class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0] * n for _ in range(n)]
        
        r = 0
        c = 0
        
        ct = 0
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirindex = 0
        
        seen = set()
        while True:
            val = ct + 1
            ans[r][c] = val
            seen.add((r, c))
            
            if ct == n**2-1:
                return ans
            else:
                ct += 1
                
                found = False
                while not found:
                    dr = dirs[dirindex][0]
                    dc = dirs[dirindex][1]
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                        found = True
                        break
                    else:
                        dirindex += 1
                        dirindex %= 4
                    
                r += dr
                c += dc