class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        charStack = []
        countStack = []
        
        currentChar = None
        currentCt = 0
        ans = []
        for ch in s:
            if currentChar is None:
                currentChar = ch
                currentCt = 1
                ans.append(ch)
            elif currentChar == ch:
                ans.append(ch)
                currentCt += 1
                
                if currentCt == k:
                    for _ in range(k):
                        ans.pop()

                    if charStack:
                        currentChar = charStack.pop()
                        currentCt = countStack.pop()
                    else:
                        currentChar = None
                        currentCt = 0
            else:
                ans.append(ch)
                charStack.append(currentChar)
                countStack.append(currentCt)
                currentChar = ch
                currentCt = 1
        
        return ''.join(ans)