class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        
        for s in ops:
            if s == '+':
                ans.append(ans[-1] + ans[-2])
            elif s == 'C':
                ans.pop()
            elif s == 'D':
                ans.append(2 * ans[-1])
            else:
                ans.append(int(s))
                
        return sum(ans)