class Solution:
    def calculate(self, s: str) -> int:
        
        num = 0
        op = None
        numStack = []
        opStack = []
        for ch in s:
            if ch == ' ':
                continue
                
            if ch.isnumeric():
                num = num * 10 + int(ch)
            else:
                if not opStack or opStack[-1] in ['+', '-']:
                    numStack.append(num)
                    opStack.append(ch)                    
                    num = 0
                else:
                    prevNum = numStack.pop()
                    prevOp = opStack.pop()
                    if prevOp == '*':
                        num = prevNum * num
                    else:
                        num = prevNum // num
                    numStack.append(num)
                    opStack.append(ch)
                    num = 0
        
        # this is a valid expression, so we always end with a number that is not put into numStack
        numStack.append(num)
        
        # if the last op in the expression is * or /, we will not be able to process it before
        # so need to check and process it here
        if opStack and opStack[-1] in ['*', '/']:
            b = numStack.pop()
            a = numStack.pop()
            op = opStack.pop()
            if op == '*':
                numStack.append(a*b)
            else:
                numStack.append(a//b)
        #print(numStack, opStack)
        
        res = numStack[0]
        for num, op in zip(numStack[1:], opStack):
            if op == '+':
                res += num
            else:
                res -= num
        return res
        
                
sol = Solution()            
print(sol.calculate('3+2*2'))