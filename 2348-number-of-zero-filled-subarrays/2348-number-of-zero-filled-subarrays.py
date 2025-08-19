class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt , ans = 0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                cnt = 0
            ans += cnt
        return ans

        