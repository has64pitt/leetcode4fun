class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        
        def getchar(k):
            return chr(k-1+ord('a'))
        
    
        possible = k - n

        if possible % 25 == 0:
            numz = possible // 25
            numa = n - numz
            return 'a' * numa + 'z' * numz
        
        else:
            """
                numa + 1 + numz = n
                numa + valother + 26*numz = k
                
                25numz + valother - 1 = k - n
                25numz = k - n + 1 - valother
                
                we want min numz, 
            """
            
            for current in range(1, 27):
                possible = k - n + 1 - current
                if possible % 25 == 0:
                    numz = possible // 25
                    numa = n - 1 - numz
                    valother = k - numa - 26 * numz
                    return 'a' * numa + getchar(valother) + 'z' * numz
            
            

    
        
        
        