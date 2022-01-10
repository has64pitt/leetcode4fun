class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        na = len(a)
        nb = len(b)        
        if na > nb:
            b = b.zfill(na)
        else:
            a = a.zfill(nb)

        a = a[::-1]
        b = b[::-1]
                    
        up = 0        
        ans = ''
        
        for cha, chb in zip(a, b):
            tmp = int(cha) + int(chb) + up
            if tmp >= 2:
                up = 1
                ans += str(tmp-2)
            else:
                up = 0
                ans += str(tmp)
        
        if up:
            ans += '1'
                
        ans = ans[::-1]
        return ans