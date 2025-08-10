class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == cnt:
                return True
        return False

        