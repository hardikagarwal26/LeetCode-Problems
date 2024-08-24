class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        temp = ""
        ans = ""
        i = 0
        while i < n:
            temp=""
            while i < n and s[i] == ' ':
                i+=1
            while i < n and s[i] != ' ':
                temp += s[i]
                i += 1
            if temp:
                if not ans:
                    ans += temp
                else:
                    ans=temp+' '+ans
        return ans
