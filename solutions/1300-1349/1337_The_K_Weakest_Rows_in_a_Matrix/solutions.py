class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        stack = []
        for index, m in enumerate(mat):
            heapq.heappush(stack, (sum(m), index))
            
        ans = []
        for _ in range(k):
            _, index = heapq.heappop(stack)
            ans.append(index)
            
        return ans