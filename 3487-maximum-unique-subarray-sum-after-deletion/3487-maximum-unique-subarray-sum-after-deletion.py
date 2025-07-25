class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        unique = set()
        neg = float('-inf')
        for i in range(len(nums)):
            if nums[i]>0:
                unique.add(nums[i])
            else:
                neg = max(neg,nums[i])
        for j in unique:
            sum += j
        if len(unique)>0:
            return sum
        else:
            return neg
        