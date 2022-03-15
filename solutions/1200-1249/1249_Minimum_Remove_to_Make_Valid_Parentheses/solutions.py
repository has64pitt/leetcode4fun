class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        
        scan from left or right
        ( -> 1
        ) -> -1
        
        if cumsum is ever -1, it needs to remove the )
        at the end, need to remove any remaining positive
        
        """
        
        ans = 0
        current = 0
        remove = []
        left = []
        for index, ch in enumerate(s):
            if ch not in ['(', ')']:
                continue
            elif ch == '(':
                current += 1
                left.append(index)
            else:
                current -= 1
            
            if current == -1:
                remove.append(index)
                current = 0
                
        if current > 0:
            remove = remove + left[-current:]
        
        return ''.join(t for index, t in enumerate(s) if index not in remove)