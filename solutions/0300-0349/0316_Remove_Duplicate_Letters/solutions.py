class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lookup = collections.defaultdict(int)
        
        for index, ch in enumerate(s):
            lookup[ch] = index
            
        stack = []
        seen = set()
        
        
        for index, ch in enumerate(s):
            if ch not in seen:
                while len(stack) > 0 and stack[-1] > ch and index < lookup[stack[-1]]:
                    prev = stack.pop()
                    seen.remove(prev)
                
                stack.append(ch)
                seen.add(ch)
                
        return ''.join(stack)
            
            

                
            