class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        arr = []
        
        for num in nums:
            if not arr or num != arr[-1]:
                arr.append(num)
        
        N = len(arr)
        if N == 1 or N == 2:
            return N
    
        if arr[1] > arr[0]:
            current = 1
        else:
            current = -1
        
        
        
        
        nums = []
        nums.append(arr[0])
        nums.append(arr[1])

        for prev, nxt in zip(arr[1:], arr[2:]):
            if current == 1:
                if nxt > prev:                
                    continue
                else:
                    current = -1                    
                    nums.append(prev)
                    
            if current == -1:
                if nxt < prev:                    
                    continue
                else:
                    current = 1
                    nums.append(prev)
              
        return len(nums)