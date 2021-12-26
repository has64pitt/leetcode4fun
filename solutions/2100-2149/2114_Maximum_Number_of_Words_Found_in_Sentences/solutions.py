from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sen in sentences:
            words = sen.split()
            res = max(res, len(words))
            
        return res