class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1:
            return True

        
        allupper = word.upper()
        alllower = word.lower()
        cond3 = word[0].upper() + word[1:].lower()
        
        if word in [allupper, alllower, cond3]:
            return True
        
        return False
