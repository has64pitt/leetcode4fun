class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        best = -1
        
        for account in accounts:
            current = sum(account)
            best = max(best, current)
            
        return best