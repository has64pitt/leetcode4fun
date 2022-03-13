class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                
        if stack:
            return False
        else:
            return True
                    