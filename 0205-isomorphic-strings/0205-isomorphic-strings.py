class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iS=[0]*200
        iT=[0]*200
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if iS[ord(s[i])] != iT[ord(t[i])]:
                return False
            iS[ord(s[i])]=i+1
            iT[ord(t[i])]=i+1
        return True