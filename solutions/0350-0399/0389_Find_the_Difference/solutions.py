class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sct = collections.Counter(s)
        tct = collections.Counter(t)
        
        for k in tct.keys():
            if tct[k] - sct[k] == 1:
                return k