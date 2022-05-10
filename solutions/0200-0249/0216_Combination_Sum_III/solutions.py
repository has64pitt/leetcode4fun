class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        
        def go(k1, n1, startnum):
            """
            return a list of list such that k1 elements add up to n1
            """
            if k1 <= 0 or n1 <= 0:
                return []
            
            elif k1 == 1:
                if n1 < 1:
                    return []
                elif startnum <= n1 <= 9:
                    return [[n1]]
                else:
                    return []
            
            
            tmp = []
            for num in range(startnum, 10):
                current = go(k1-1, n1-num, num+1)
                if current:
                    for icurrent in current:
                        tmp.append([num] + icurrent)
                        
            return tmp
    
        return go(k, n, 1)
                    