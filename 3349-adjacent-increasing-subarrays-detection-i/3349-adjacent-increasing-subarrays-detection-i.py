class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        last = 0
        boo = False
        while i < n:
            count = 1
            j = i + 1
            while j < n and nums[j] > nums[j-1] and count < k:
                j += 1
                count += 1

            if count == k:
                if boo : return True
                boo = True
                i = j
            else:
                boo = False
                last += 1
                i = last

        return False
        