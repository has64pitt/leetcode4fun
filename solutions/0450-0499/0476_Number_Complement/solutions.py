class Solution:
    def findComplement(self, num: int) -> int:
        numbin = bin(num)[2:]
        
        if '0' not in numbin:
            return 0
        else:
            index0 = numbin.index('0')
            numbin = numbin[index0:]
            
        ans = 0
        for index, ch in enumerate(numbin[::-1]):
            if ch == '0':
                ans += 2 ** index
            
        #print(num, numbin)
        return ans