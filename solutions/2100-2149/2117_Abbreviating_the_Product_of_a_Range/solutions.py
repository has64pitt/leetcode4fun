class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        """
        3 sub-tasks
        1) get trailing 0
        2) get last 5 digits
        3) get first 5 digits
        """
        
        
        pre = suf = 1
        pow10 = 0
        pow2 = 0
        pow5 = 0
        res = 1
        
        # part 1, get training 0
        for num in range(left, right + 1):
            while num % 10 == 0:
                num = num // 10
                pow10 += 1
                
            while num % 2 == 0:
                num = num // 2
                pow2 += 1
                
            while num % 5 == 0:
                num = num // 5
                pow5 += 1
                
            mn = min(pow2, pow5)
            pow10 += mn
            pow5 -= mn
            pow2 -= mn
            
        # part 2, get last 5 digits            
        mod = 10 ** 10
        res_suf = 1
        for num in range(left, right + 1):
            while num % 10 == 0:
                num = num // 10

            res_suf *= num

            while res_suf % 10 == 0:
                res_suf = res_suf // 10

            res_suf %= mod

        # part 3, get first 5 digits            
        res_pre = 1
        nlen = 0
        nbits = 20
        for num in range(left, right+1):
            res_pre *= num            
            res_pre_len = len(str(res_pre))
            if res_pre_len > nbits:
                nlen += res_pre_len - nbits
            res_pre = int(str(res_pre)[:nbits])
            
        #print(res_pre, nlen, pow10)
        if nlen + len(str(res_pre)) - pow10 <= 10:
            while res_pre % 10 == 0:
                res_pre = res_pre // 10
            return str(res_pre) + 'e' + str(pow10)
        
        else:
            #print(res_suf)
            a = str(res_pre)[:5]
            b = str(res_suf).zfill(5)[-5:]
            return a + '...' + b + 'e' + str(pow10)
            
            
sol = Solution()            

print(sol.abbreviateProduct(1, 4))
print(sol.abbreviateProduct(2, 11))
print(sol.abbreviateProduct(999998, 1000000))
            
                
            
        
            
            
            