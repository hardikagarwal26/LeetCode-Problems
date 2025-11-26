class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums):
            val = target - n
            if val in hmap:
                return [hmap[val] , i]
            hmap[n] = i
        return

            
            
        