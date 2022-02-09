class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
                  
        ans = set()
        seen = set()
        
        for num in nums:
            if num + k in seen and (num, num+k) not in ans:
                ans.add((num, num+k))
            if num - k in seen and (num-k, num) not in ans:
                ans.add((num-k, num))
            seen.add(num)
            
        return len(ans)