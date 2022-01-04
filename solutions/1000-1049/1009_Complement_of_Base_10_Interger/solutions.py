class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        nstr = bin(n)[2:]
        nstr = nstr.lstrip('1')        

        if not nstr:
            return 0
        
        s = ''
        for ch in nstr:
            if ch == '1':
                s += '0'
            else:
                s += '1'
            
        return int(s, 2)    