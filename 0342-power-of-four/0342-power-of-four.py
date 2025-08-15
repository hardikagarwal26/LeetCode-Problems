class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n,4) % 1 == 0
        # x = 1
        # while x < n:
        #     x *= 4
        # return x == n

        