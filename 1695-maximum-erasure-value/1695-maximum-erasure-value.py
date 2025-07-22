class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        vis = set()
        curr = 0
        maxsum = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in vis :
                vis.remove(nums[l])
                curr -= nums[l]
                l+=1
            vis.add(nums[r])
            curr+=nums[r]
            maxsum = max(maxsum,curr)
        return maxsum
        