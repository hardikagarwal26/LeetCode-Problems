class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        cnt = 0
        while j+1 < n:
            if (nums[i] < nums[j] and nums[j] > nums[j+1]) or (nums[i] > nums[j] and nums[j]<nums[j+1]):
                cnt += 1
                i=j
            j += 1
        return cnt



        