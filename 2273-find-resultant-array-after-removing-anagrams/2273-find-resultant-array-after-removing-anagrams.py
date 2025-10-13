class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)

        c = {}
        for i in range(n): c[i] = Counter(words[i])

        res = [words[0]]
        for i in range(1,n):
            if c[i] != c[i-1]:
                res.append(words[i])
        return res