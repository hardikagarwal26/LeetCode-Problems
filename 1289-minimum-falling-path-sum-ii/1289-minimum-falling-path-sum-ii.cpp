class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n=grid.size();
        int min1=0;
        int min2=n-1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j] < grid[i][min1])
                {
                    min2=min1;
                    min1=j;
                }
                else if(grid[i][j]<grid[i][min2] && j!=min1)
                min2=j;
            }
            for(int j=0;j<n;j++)
            {
                if(i+1<n)
                {
                    if(j==min1)
                    grid[i+1][j]+=grid[i][min2];
                    else
                    grid[i+1][j]+=grid[i][min1];
                }
            }
        }
        return grid[n-1][min1];
    }
};