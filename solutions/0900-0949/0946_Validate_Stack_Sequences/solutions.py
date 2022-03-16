class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        
        stack = []
        
        p1 = 0
        p2 = 0
        
        while p1 < N and p2 < N:
            if not stack or stack[-1] != popped[p2]:
                stack.append(pushed[p1])
                p1 += 1
            else:
                stack.pop()
                p2 += 1
        
        while p2 < N:
            if stack[-1] != popped[p2]:
                return False
            else:
                stack.pop()
                p2 += 1
                
        return True
                