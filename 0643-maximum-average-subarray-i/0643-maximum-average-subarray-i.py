class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0.0
        l = 0
        s = 0
        for r in range(k):
            s += nums[r]
        mavg = s/k

        for i in range(k,len(nums)):
            s += nums[i]
            s -= nums[i-k]
            avg = s/k
            mavg = max(mavg,avg)
        return mavg

        