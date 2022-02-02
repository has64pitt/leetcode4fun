class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.Counter(p)
        
        pset = set(p)
        keys = len(pset)
        
        N1 = len(s)
        N2 = len(p)
        
        matched = 0
        found = collections.defaultdict(int)
        
        ans = []
        for index in range(N1):
            char = s[index]
            found[char] += 1
            
            if char in pset and need[char] == found[char]:
                matched += 1
            
            if index - N2 >= 0:
                pchar = s[index-N2]
                if pchar in pset and need[pchar] == found[pchar]:
                    matched -= 1                    
                found[pchar] -= 1                    
            
            if matched == keys:
                ans.append(index-N2+1)
                
        return ans
                