class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        
        if N < 3:
            return False
        
        mx = max(arr)
        if arr.count(mx) > 1:
            return False
        
        ind = arr.index(mx)
        
        if ind == 0 or ind == N-1:
            return False
        
        
        for i in range(ind):
            if arr[i] >= arr[i+1]:
                return False
            
        for i in range(ind, N-1):
            if arr[i] <= arr[i+1]:
                return False            
            
        return True