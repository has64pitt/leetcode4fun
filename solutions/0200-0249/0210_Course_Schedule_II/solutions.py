import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inDict = collections.defaultdict(int)
        outDict = collections.defaultdict(list)
        
        for nxt, prev in prerequisites:
            inDict[nxt] += 1
            outDict[prev].append(nxt)
            
            
        stack = [i for i in range(numCourses) if inDict[i] == 0]
        res = []
        
        while stack:
            current = stack.pop()
            res.append(current)
            
            for nxt in outDict[current]:
                inDict[nxt] -= 1
                if inDict[nxt] == 0:
                    stack.append(nxt)
                    
        if len(res) == numCourses:
            return res
        else:
            return []