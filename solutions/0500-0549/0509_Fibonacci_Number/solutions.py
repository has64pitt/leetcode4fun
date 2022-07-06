class Solution:
    def fib(self, n: int) -> int:
        
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        arr = [0, 1]
        
        for i in range(n-1):
            arr.append(arr[-1] + arr[-2])
            
        return arr[-1]