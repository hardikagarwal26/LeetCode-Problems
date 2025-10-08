class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for s in spells:
            l , r = 0, len(potions) - 1
            idx = len(potions)
            while l <= r:
                m = (l+r)//2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            ans.append(len(potions) - idx)
        return ans
        