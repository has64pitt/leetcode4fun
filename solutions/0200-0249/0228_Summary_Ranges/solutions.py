class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        
        prev = None
        current = []
        for num in nums:
            if prev is None:
                prev = num
                current = [prev]
            elif prev + 1 == num:
                if len(current) == 1:                    
                    current.append(num)
                else:
                    current[-1] = num
                prev = num
            else:
                if len(current) == 1:
                    ans.append(str(current[0]))
                else:
                    ans.append(str(current[0]) + '->' + str(current[-1]))                    
                current = [num]
                prev = num

        
        if len(current) == 1:
            ans.append(str(current[0]))
        elif len(current) >= 2:
            ans.append(str(current[0]) + '->' + str(current[-1]))
                
        return ans