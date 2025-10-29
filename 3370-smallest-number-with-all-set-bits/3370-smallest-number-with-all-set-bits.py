class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while n > ans:
            ans = (ans << 1) | 1
        return ans
        