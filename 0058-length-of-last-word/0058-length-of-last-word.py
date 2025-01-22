class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i , c = len(s)-1 , 0
        while s[i] == " ":
            i-=1
        while i>=0 and s[i]!=" ":
            c+=1
            i-=1
        return c
        