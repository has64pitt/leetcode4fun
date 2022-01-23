class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nlow = len(str(low))
        nhigh = len(str(high))
        
        ans = []
        
        low_start = int(str(low)[0])
        
        for n in range(nlow, nhigh + 1):
            if n == nlow:
                start = low_start
            else:
                start = 1
            
            mx = 10 - n
            for istart in range(start, mx + 1):
                tmp = [str(t) for t in range(istart, istart + n)]
                tmp = int(''.join(tmp))
                if tmp < low:
                    continue
                if tmp > high:
                    return ans                
                ans.append(int(tmp))
                
        return ans