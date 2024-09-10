class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sort = sorted(char_count,key=char_count.get,reverse=True)
        ans=''
        for i in sort:
            ans+=i*char_count[i]
        return ans