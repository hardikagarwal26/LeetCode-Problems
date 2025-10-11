from functools import lru_cache
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        mp = Counter(power)
        vec = sorted((k, k * v) for k, v in mp.items())
        n = len(vec)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 0
            not_take = solve(i + 1)
            take = vec[i][1]
            j = i + 1
            while j < n and vec[j][0] - vec[i][0] <= 2:
                j += 1
            take += solve(j)
            return max(take, not_take)

        return solve(0)