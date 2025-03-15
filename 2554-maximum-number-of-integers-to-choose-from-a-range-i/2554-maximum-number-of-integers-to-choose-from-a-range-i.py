class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        tsum = 0
        cnt = 0
        for i in range(1,n+1):
            if i in ban:
                continue
            tsum +=i
            if tsum > maxSum:
                break
            cnt += 1
        return cnt