from typing import Collection, List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s) 
        
        ans = []

        indexDict = Collection.defaultdict(list)
        for left in range(n):
            for right in range(left, n):
                possible = s[left:right+1]
                if possible == possible[::-1]:
                    indexDict[left].append(right)
                    
        def go(index, arr):
            if index == n:
                ans.append(arr[:])
                return
            
            for nxt in indexDict[index]:
                go(nxt+1, arr + [s[index:nxt+1]])
                    
        go(0, [])
        return ans