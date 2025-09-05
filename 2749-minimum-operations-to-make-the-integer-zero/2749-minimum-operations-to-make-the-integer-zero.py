class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1,61):
            d = num1 - i*num2
            if d < 0:
                continue
            b = bin(d).count("1")
            if i>=b and i <= d:
                return i
        return -1
        