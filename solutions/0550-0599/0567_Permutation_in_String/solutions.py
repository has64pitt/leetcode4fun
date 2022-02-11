class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        
        if N1 > N2:
            return False
        
        ct1 = collections.Counter(s1)
        ct2 = collections.defaultdict(int)
        
        target = len(list(ct1.keys()))
        matched = 0
        
        for i in range(N2):
            current = s2[i]
            ct2[current] += 1
            
            if current in ct1 and ct1[current] == ct2[current]:
                matched += 1
                
            if i >= N1:
                prev = s2[i-N1]
                if prev in ct1 and ct1[prev] == ct2[prev]:
                    matched -= 1                
                ct2[prev] -= 1
                
            if matched == target:
                return True
            
        return False