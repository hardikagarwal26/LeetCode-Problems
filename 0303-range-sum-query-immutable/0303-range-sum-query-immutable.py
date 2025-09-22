class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix.append(curr)
        

    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix[left - 1] if left > 0 else 0
        r = self.prefix[right]
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)