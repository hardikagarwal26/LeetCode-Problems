class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        gpair = 0
        tpair = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            tpair += i
            gpair += count[nums[i] - i]
            count[nums[i] - i] += 1
        return tpair - gpair
        