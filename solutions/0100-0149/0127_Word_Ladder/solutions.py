class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        
        n = len(beginWord)
        
        wordDict = collections.defaultdict(list)
        
        for word in set(wordList):
            
            for i in range(n):
                key = word[:i] + '*' + word[i+1:]
                wordDict[key].append(word)
                
        
        queue = collections.deque()
        queue.append( (beginWord,1) )
        
        seen = set()
        seen.add(beginWord)
        
        while queue:
            current, ans = queue.popleft()
            
            if current == endWord:
                return ans
                        
            for i in range(n):
                key = current[:i] + '*' + current[i+1:]
                for nxt in wordDict[key]:
                    if nxt not in seen:
                        queue.append((nxt, ans+1))
                        seen.add(nxt)
        
        return 0