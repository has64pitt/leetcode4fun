class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: -x[1])        
        
        current = 0
        ans = 0
        
        for n, unit in boxTypes:
            if current + n <= truckSize:
                current += n
                ans += n * unit
            else:
                add = truckSize - current
                ans += add * unit
                return ans
        
        return ans