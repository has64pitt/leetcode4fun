class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        """
        TAG: DP
        """
        
        
        counts = [[0] * n for _ in range(5)]

        """
        counts[i][j] tells us for length of j+1, ending at vow[i], how many of these string
        """
        
        for i in range(5):
            counts[i][0] = 1
            
        for l in range(1, n):
            counts[0][l] += counts[0][l-1]
            counts[1][l] += counts[0][l-1]
            counts[2][l] += counts[0][l-1]
            counts[3][l] += counts[0][l-1]
            counts[4][l] += counts[0][l-1]
            
            counts[1][l] += counts[1][l-1]
            counts[2][l] += counts[1][l-1]
            counts[3][l] += counts[1][l-1]
            counts[4][l] += counts[1][l-1]            
            
            counts[2][l] += counts[2][l-1]
            counts[3][l] += counts[2][l-1]
            counts[4][l] += counts[2][l-1]                        
            
            counts[3][l] += counts[3][l-1]
            counts[4][l] += counts[3][l-1]            
            
            counts[4][l] += counts[4][l-1]                        
            
        
        
        return sum(t[-1] for t in counts)