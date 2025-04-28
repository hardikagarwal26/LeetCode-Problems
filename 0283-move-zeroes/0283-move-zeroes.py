class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for c , val in enumerate(nums):
            if val != 0:
                nums[a] ,  nums[c] = nums[c] , nums[a]
                a+=1
        