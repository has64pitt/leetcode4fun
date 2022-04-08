class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = []
        self.k = k
        
        for index, val in enumerate(nums):
            if index < k:
                heapq.heappush(self.hq, val)
            else:
                if val > self.hq[0]:
                    heapq.heappop(self.hq)
                    heapq.heappush(self.hq, val)
                    
                    
    def add(self, val: int) -> int:
        
        if len(self.hq) < self.k:
            heapq.heappush(self.hq, val)
            return self.hq[0]    
        
        if val > self.hq[0]:
            heapq.heappop(self.hq)
            heapq.heappush(self.hq, val)
        
        return self.hq[0]