class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = 0
        for i in range(len(word)):
            if word[i] == ch:
                pos = i+1
                break
        nstr = word[0:pos]
        return nstr[::-1] + word[pos:len(word)]
        
    