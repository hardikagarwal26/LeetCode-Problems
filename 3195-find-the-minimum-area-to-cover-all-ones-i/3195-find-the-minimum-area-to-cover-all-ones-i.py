class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        sh , sw = 1001 , 1001
        eh , ew = -1,-1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    sh = min(sh , i)
                    sw = min(sw , j)
                    eh = max(eh , i)
                    ew = max(ew , j)
        return (eh - sh + 1) * (ew - sw + 1)
