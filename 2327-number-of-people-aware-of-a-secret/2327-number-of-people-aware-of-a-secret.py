class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0]*(n+1)
        dp[1] = 1
        act = 0
        for day in range(2,n+1):
            if day - delay > 0:
                act = (act + dp[day - delay])% mod
            if day - forget > 0:
                act = (act - dp[day - forget])% mod
            dp[day] = act
        total = sum(dp[n - forget + 1 : n+1]) % mod
        return total
        