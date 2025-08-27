from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid):
        n, m = len(grid), len(grid[0])
        dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]
        
        @lru_cache(None)
        def solve(i, j, direction, turn, search):
            nx, ny = i + dirs[direction][0], j + dirs[direction][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != search:
                return 1  
            
            ans = solve(nx, ny, direction, turn, 2 - search)
            if turn > 0:
                ans = max(ans, solve(nx, ny, (direction+1) % 4, turn-1, 2 - search))
            return ans + 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, solve(i, j, d, 1, 2))
        return ans