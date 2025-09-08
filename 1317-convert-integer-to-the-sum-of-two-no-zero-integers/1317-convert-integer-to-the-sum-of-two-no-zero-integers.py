class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            j = n - i
            if not '0' in str(i) and not '0' in str(j):
                return [i,j]

        