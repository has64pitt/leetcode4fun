class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        N = len(ratings)
        
        if N == 1:
            return 1
        
        ans = [None] * N
        
        arr = []
        for index, rating in enumerate(ratings):
            arr.append((rating, index))
        
        arr.sort()
        
        for rating, index in arr:
            if index > 0 and index < N-1:                
                left = 0
                right = 0
                if ratings[index-1] < rating:                
                    if ans[index-1] is not None:
                        left = ans[index-1]

                if ratings[index+1] < rating:    
                    if ans[index+1] is not None:
                        right = ans[index+1]
                
                ans[index] = max(left, right) + 1

            elif index == 0:                
                right = 0
                if ratings[index+1] < rating:    
                    if ans[index+1] is not None:
                        right = ans[index+1]
                
                ans[index] = right + 1

            else:
                left = 0
                if ratings[index-1] < rating:    
                    if ans[index-1] is not None:
                        left = ans[index-1]
                
                ans[index] = left + 1
        
        return sum(ans)
                
                    
                    
                
                
                    