class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def diag(r , c , order = True):
            arr = []
            i , j = r, c
            while i<n and j<n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            arr.sort(reverse = order)
            for val in arr:
                grid[r][c] = val
                r += 1
                c += 1
        
        for i in range(n):
            diag(i,0)
        for i in range(1,n):
            diag(0,i,order = False)
        return grid