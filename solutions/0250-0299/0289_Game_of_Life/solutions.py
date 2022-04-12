class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        
        ans = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                livect = 0
                
                
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            if board[nr][nc] == 1:
                                livect += 1
                
                if board[r][c] == 1:
                    if livect < 2 or livect > 3:
                        ans[r][c] = 0
                    else:
                        ans[r][c] = 1
                else:
                    if livect == 3:
                        ans[r][c] = 1
                    else:
                        ans[r][c] = 0
                        
        for r in range(m):
            for c in range(n):
                board[r][c] = ans[r][c]