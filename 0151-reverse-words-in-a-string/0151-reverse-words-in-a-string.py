class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ans = ""
        i = 0
        while i<n:
            word = ""
            while i<n and s[i] == ' ':
                i+=1
            while i<n and s[i]!=' ':
                word+=s[i]
                i+=1
            if len(word)>0:
                ans = word + " "+ans
        return ans.strip()
            
            

        