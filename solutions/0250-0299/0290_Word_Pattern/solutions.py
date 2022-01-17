class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        word2patDict = {}
        pat2wordDict = {}
        for pat, word in zip(pattern, words):
            if pat not in pat2wordDict and word not in word2patDict:
                pat2wordDict[pat] = word
                word2patDict[word] = pat
            elif pat not in pat2wordDict or word not in word2patDict:
                return False
            else:
                if pat2wordDict[pat] != word or word2patDict[word] != pat:
                    return False
            
        return True
            