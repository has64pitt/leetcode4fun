class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        N = len(people)
        
        p1 = 0
        p2 = N-1
        
        ans = 0
        
        while p1 < p2:            
            ans += 1            
            if people[p1] + people[p2] <= limit:
                p1 += 1
            p2 -= 1
                    
        if p1 == p2:
            ans += 1
            
            
        return ans