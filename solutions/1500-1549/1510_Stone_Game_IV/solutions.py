class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        imaging you are alice, now it is your turn
        
        n = 1, you win
        n = 2, you lose
        n = 3, you win
        n = 4, you win
        n = 5, you lose
        n = 6, you win
        """
        
        
        dp = [False] * (n+1)
        sqrtn_plus1 = int(sqrt(n)) + 1
        
        for i in range( n+1):
            if dp[i] is False:
                for t in range(1, sqrtn_plus1+1):
                    nxt = i + t ** 2
                    if nxt <= n:
                        dp[nxt] = True
        

        return dp[-1]