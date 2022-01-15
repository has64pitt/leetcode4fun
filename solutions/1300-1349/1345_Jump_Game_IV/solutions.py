import collections
from typing import Collection, List


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        stack = []
        
        for index, num in enumerate(nums):
            if len(stack) < 2:
                stack.append(index)            
            elif num == nums[stack[-1]] and num == nums[stack[-2]]:
                stack.pop()
                stack.append(index)
            else:
                stack.append(index)
        
                
        
        jump = collections.defaultdict(list)
        
        for index in stack:
            jump[nums[index]].append(index)
            
        queue = collections.deque([0])
        seen = set()
        valSeen = set()
        
        ans = 0
        while queue:
            qlen = len(queue)            
            #print(queue)
            for _ in range(qlen):
                current = queue.popleft()
                
                
                seen.add(current)
                if current == N-1:
                    return ans
                
                if current > 0 and current - 1 not in seen:
                    queue.append(current-1)
                    seen.add(current-1)
                    
                if current < N-1 and current + 1 not in seen:
                    queue.append(current+1)
                    seen.add(current+1)
                    
                val = nums[current]
                
                if val not in valSeen:
                    valSeen.add(val)
                    for ind in jump[val]:
                        if ind not in seen:
                            queue.append(ind)
                            seen.add(ind)
                        
            ans += 1
            
    
                        

            
            