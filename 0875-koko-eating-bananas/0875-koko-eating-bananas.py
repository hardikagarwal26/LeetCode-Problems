class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
            if hrs <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
        