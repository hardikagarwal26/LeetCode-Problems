class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in s:
            if i in "aeiou":
                return True
        return False
        