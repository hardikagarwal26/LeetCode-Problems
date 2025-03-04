class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            d = target - n
            if d in hashmap:
                return [hashmap[d],i]
            hashmap[n] = i
        return