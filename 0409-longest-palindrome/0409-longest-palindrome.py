class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0
        for i in s:
            count[i]+=1
            if count[i]%2 == 0:
                ans+=2
        for cnt in count.values():
            if cnt%2:
                ans+=1
                break
        return ans
            