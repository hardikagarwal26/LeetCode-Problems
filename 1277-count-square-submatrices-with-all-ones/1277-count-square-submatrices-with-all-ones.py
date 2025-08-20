class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row , col = len(matrix) , len(matrix[0])
        dp = defaultdict(int)
        ans = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c]:
                    dp[(r,c)] = 1 + min(
                        dp[(r-1 , c)],
                        dp[(r-1 , c-1)],
                        dp[(r , c-1)]
                    )
                    ans += dp[(r,c)]
        return ans
        