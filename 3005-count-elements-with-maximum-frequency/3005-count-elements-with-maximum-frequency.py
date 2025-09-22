class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101
        maxF = 0
        for num in nums:
            freq[num] += 1
            maxF = max(maxF , freq[num])
        ans = 0
        for f in freq:
            if f == maxF:
                ans += maxF
        return ans