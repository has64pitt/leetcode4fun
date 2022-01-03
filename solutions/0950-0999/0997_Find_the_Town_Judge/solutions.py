from typing import Collection, List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ct = Collection.defaultdict(int)
        exclude = set()
        for frm, to in trust:
            ct[to] += 1
            exclude.add(frm)
            
        allpeople = set(range(1, n+1))
        
        possible = allpeople - exclude
        
        if not possible:
            return -1
        if len(possible) > 1:
            return -1
        if ct[list(possible)[0]] != n-1:
            return -1
        
        return list(possible)[0]