class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs[0])
        ans=""
        for i in range(n):
            if strs[0][i] == strs[-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans