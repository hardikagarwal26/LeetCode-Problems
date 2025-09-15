class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        brokenLetters = set(brokenLetters)
        cnt = 0
        for w in text:
            for c in w:
                if c in brokenLetters:
                    cnt += 1
                    break
                    
        return len(text) - cnt
            

        