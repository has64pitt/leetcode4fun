class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        

        level = [[0] * k for k in range(1, 102)]
        level[0][0] = poured
        
        for row in range(query_row+1):
            for col in range(row+1) :
        
                overflow = level[row][col] - 1
                
                if overflow > 0:
                    level[row+1][col] += 0.5*overflow
                    level[row+1][col+1] += 0.5 * overflow
                    
        return min(1, level[query_row][query_glass])