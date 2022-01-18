from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        ct = 0 # how many consecutive 0 
        res = 0
        
        
        flowerbed = [0] + flowerbed + [0]
        # 1, 2 -> 0
        # 3, 4 -> 1
        # 5, 6 -> 2
        for num in flowerbed:
            if num == 0:
                ct += 1 
            else:
                res += max(0, (ct+1) // 2 - 1)
                ct = 0
        
        res += max(0, (ct+1) // 2 - 1)
        return res >= n
    
        """
        ct = 
        0, 1, 2 -> 0
        3, 4 -> 1
        5, 6 -> 2
        """