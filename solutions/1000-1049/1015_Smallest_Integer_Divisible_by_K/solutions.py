class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        seen = set()
        n = 1
        
        while True:
            r = n % k
            
            if r == 0:
                return len(str(n))
            
            if r in seen:
                return -1
            else:
                seen.add(r)

            n = 10 * n + 1